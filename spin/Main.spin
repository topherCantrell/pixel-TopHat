CON
  _clkmode        = xtal1 + pll16x
  _xinfreq        = 5_000_000            

CON

    USE_WEB     =   1

    pinWEBIN    =   0 ' From Pi0 to both CPUs
    pinWEBOUT   =   2 ' Not actually connected

    pinSYNCin   =  10 ' Board header
    pinSYNCout  =  11 ' Board header
     
    pinS1       =  19 ' Purple
    pinS2       =  20 ' White
    pinS3       =  21 ' Yellow
    pinS4       =  22 ' Gray
    '
    pinCS       =  24 ' PCB
    pinDI       =  25 ' PCB
    pinSCLK     =  26 ' PCB
    pinDO       =  27 ' PCB          

OBJ    
    STRIPA   : "NeoPixelStrip"
    STRIPB   : "NeoPixelStrip"
    STRIPC   : "NeoPixelStrip"
    STRIPD   : "NeoPixelStrip"
    '
    PST      : "Parallax Serial Terminal"
    WEB      : "Parallax Serial Terminal"
    SD       : "SDCard"      

VAR
    byte animationMap[512]    ' First disk sector: map of animation names to start sectors
    byte movieConfig[512]     ' Info about the current movie: number of frames, delay between frames
    byte colorPalette[1024]   ' Current movie's color palette
    byte adjustedColors[1024] ' Color palette adjusted for brightness TODO
    byte frameBuffer[1024*2]  ' Two frame buffers (loading and drawing)
    
    long currentFrameCount    ' How many frames left in current movie
    long currentSector        ' Cursor to the disk
    long currentDelay         ' Delay between frames for this movie

    long bufferOffset         ' Pointer to the frame buffer being drawn
    long bufferNextOffset     ' Pointer to the frame buffer being filled from disk

    long syncSignalMy         ' The current sync value I am sending 
    long syncSignalOther      ' The current sync value the other processor is sending

    long startCurrentMovie    ' In case we need to repeat a movie
    long currentColorMult

PUB main | i, j

  ' Initialize the sync
  dira[pinSYNCout] := 1
  outa[pinSYNCout] := 0         
  dira[pinSYNCin] := 0  
  syncSignalMy := 0
  syncSignalOther := 0

  ' Drive the data lines low to start
  outa[pinS1] := 0
  dira[pinS1] := 1
  outa[pinS2] := 0
  dira[pinS2] := 1
  outa[pinS3] := 0
  dira[pinS3] := 1
  outa[pinS4] := 0
  dira[pinS4] := 1    

  ' Initialize the pixel drivers
  STRIPA.init
  STRIPB.init
  STRIPC.init
  STRIPD.init

  ' Blank all pixels
  STRIPA.draw(2, @BLANKGREEN, @BLANKPIX, pinS1, 256)
  STRIPB.draw(2, @BLANKGREEN, @BLANKPIX, pinS2, 256)
  STRIPC.draw(2, @BLANKGREEN, @BLANKPIX, pinS3, 256)
  STRIPD.draw(2, @BLANKGREEN, @BLANKPIX, pinS4, 256)
    
  PauseMSec(2000) ' For development - give user time to switch to terminal

  ' Blank all pixels
  STRIPA.draw(2, @BLANKPIX, @BLANKPIX, pinS1, 256)
  STRIPB.draw(2, @BLANKPIX, @BLANKPIX, pinS2, 256)
  STRIPC.draw(2, @BLANKPIX, @BLANKPIX, pinS3, 256)
  STRIPD.draw(2, @BLANKPIX, @BLANKPIX, pinS4, 256)
    
  PST.start(115200)

  PST.str(string("PixelHat 2018-1",13))

  {
  if USE_WEB==1
    PST.str(string("Fixed wait time for PiZero ...............................................................|",13))   
    repeat i from 1 to 90 ' 90 seconds
      PauseMSec(1000)    
      PST.char($2E)
    PST.str(string(13,"Done waiting for PiZero.",13))
    }                       
  
  WEB.StartRxTx(pinWEBIN, pinWEBOUT, 0, 115200)

  ' frameBuffer used for scratch during the startup process
  i := SD.start(@frameBuffer, pinDO, pinSCLK, pinDI, pinCS)
  if i<>0
    showError(string("Error mounting SD card"),1)
  else
    PST.str(string("Mounted SD card: OK",13))
      
  ' Map of all animations on the disk
  SD.readFileSectors(@animationMap,0,1)
  i := SD.waitForDone
  if i<>0
    showError(string("DISK ERROR 1"),i)
  PST.str(string("Read animation map: OK",13))  
      
  ' First animation starts in the next sector
  currentSector := 1
  currentColorMult := 6 ' Default color scale is "as is"
    
  PST.str(string("Starting main loop.",13))
      
  repeat  
    
    i := SD.waitForDone ' We might be in the middle of a cache operation from below
    if i<>0
      showError(string("DISK ERROR 2"),i)

    ' Read the info on the movie
    startCurrentMovie := currentSector ' In case we need to repeat
    SD.readFileSectors(@movieConfig,currentSector,1)
    currentSector := currentSector + 1
    i := SD.waitForDone ' We need this info
    if i<>0
      showError(string("DISK ERROR 3"),i)
    
    currentFrameCount := long[@movieConfig]
    currentDelay := long[@movieConfig+4]

    if currentFrameCount == 0
      ' End of all animations -- restart at the beginning of the disk)
      currentSector := 1      
      next

    ' Read the color palette
    SD.readFileSectors(@colorPalette,currentSector,2)
    currentSector := currentSector + 2
    i := SD.waitForDone ' We need this info
    if i<>0
      showError(string("DISK ERROR 4"),i)
    adjustColors

    ' Current and back buffer
    bufferOffset := 0
    bufferNextOffset := 1024

    ' Read the first frame. We have to wait on this one.
    SD.readFileSectors(@frameBuffer,currentSector,2)
    currentSector := currentSector + 2 
    i := SD.waitForDone
    if i<>0
      showError(string("DISK ERROR 5"),i)

    repeat    

      if USE_WEB==1
        ' Check for serial command      
        if WEB.RxCount > 0
          PST.str(string("Waiting on rest of line ... "))
          WEB.StrIn(@movieConfig)
          j := byte[@movieConfig]
          if j=>$30 and j=<$39
            ' This is a brightness command
            currentColorMult := j - $30
            PST.str(string(" ... setting brightness to "))
            PST.hex(currentColorMult,2)
            PST.char(13)
            adjustColors
          else
            ' Switch to new movie
            PST.str(string(" ... got:"))
            PST.str(@movieConfig)
            PST.str(string(":",13))
            currentSector := getAnimationSector(@movieConfig)
            quit          
             
      ' Start loading the next frame in the back buffer
      i:=SD.waitForDone ' Hopefully this never waits (long delay coming up)
      if i<>0
        showError(string("DISK ERROR 6"),i)          
      SD.readFileSectors(@frameBuffer+bufferNextOffset,currentSector,2)
      currentSector := currentSector + 2          

      ' Make sure the two CPUs draw at the same time
      syncToOther            
      
      ' Draw the current frame
      STRIPA.draw(2, @adjustedColors, @frameBuffer    +bufferOffset, pinS1, 256)
      STRIPB.draw(2, @adjustedColors, @frameBuffer+256+bufferOffset, pinS2, 256)
      STRIPC.draw(2, @adjustedColors, @frameBuffer+512+bufferOffset, pinS3, 256)
      STRIPD.draw(2, @adjustedColors, @frameBuffer+768+bufferOffset, pinS4, 256)  
      
      PauseMSec(currentDelay)
        
      ' Count the frames      
      currentFrameCount := currentFrameCount - 1
      if currentFrameCount == 0
        ' End of this sequence -- break out to load next sequence          
        if long[@movieConfig+8] == 0            ' 0 : Fall into next movie
          currentSector := currentSector - 2
        else
          currentSector := long[@movieConfig+8] ' N : Go to sector N                   
        quit

      ' Swap the back buffer and the current buffer
      i := bufferOffset
      bufferOffset := bufferNextOffset
      bufferNextOffset := i

PRI adjustColors | i,j, k, x
  repeat i from 0 to 256 ' 256 longs = 1024 bytes
    k := long[@colorMult+currentColorMult*4] ' Multiplier for each byte in color
    repeat x from 0 to 3                     ' All four bytes (wRGB)
      j := byte[@colorPalette+i*4+x] * 1_00
      j := (j * k) / 1_00_00
      byte[@adjustedColors+i*4+x] := j    
    
PRI syncToOther | i
  
  ' Flip our sync output
  if syncSignalMy == 1
    syncSignalMy := 0
  else
    syncSignalMy := 1
  outa[pinSYNCout] := syncSignalMy

  'PST.str(string("Flipped my sync to "))
  'PST.hex(syncSignalMy,2)
  'PST.char(13)
  
  'PST.str(string("Waiting for other ..."))
  
  ' Now wait for the input to flip
  repeat while ina[pinSYNCin] == syncSignalOther
  
  'PST.str(string(" ... flipped.",13))
  syncSignalOther := ina[pinSYNCin]

{
PRI dumpSD(p) | i

  repeat i from 0 to 8
    PST.hex(byte[p+i],2)
    PST.char(32)
}       

PRI strCmp(a,b)
' Compare two strings. Return 1 if the same or 0 if not  
  repeat
    if byte[a] <> byte[b]
      return 0
    if byte[a] == 0
      return 1
    a := a+1
    b := b+1

PRI getAnimationSector(p) | i
' Find the entry in the animation map. Return the info sector (or 1 if not found)    
  i := 16 ' First entry in table                         
  repeat
    if byte[@animationMap+i] == 0
      return 1 ' Couldn't find it ... go back to the first
    if strCmp(@animationMap+i,p)==1
      return long[@animationMap+i+12]
    i := i + 16 ' Next entry  
     
PRI PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)

PRI showError(msg, code) | i, p
  PST.str(msg)
  PST.str(string(": "))
  PST.hex(i,4)
  PST.char(13)
  i := 128
  p := 2
  byte[@BLANKPIX]    := 1
  byte[@BLANKPIX+1]  := 1
  byte[@BLANKPIX+10] := 1
  repeat while i > 0
    if (code & i) > 0
      byte[@BLANKPIX+p] := 4
    p := p + 1
    i := i / 2
  STRIPA.draw(2, @ERRCOLLORS, @BLANKPIX, pinS1, 256)
  STRIPB.draw(2, @ERRCOLLORS, @BLANKPIX, pinS2, 256)
  STRIPC.draw(2, @ERRCOLLORS, @BLANKPIX, pinS3, 256)
  STRIPD.draw(2, @ERRCOLLORS, @BLANKPIX, pinS4, 256)

  repeat       

DAT

colorMult
  long  10    ' 0.10  
  long  20    ' 0.20
  long  50    ' 0.50
  long  40    ' 0.40
  long  70    ' 0.70
  long  90    ' 0.90
  long 100    ' 1.00 <- Default
  long 125    ' 1.25
  long 150    ' 1.50
  long 200    ' 2.00

ERRCOLLORS
  long $00_00_00_00
  long $00_00_00_40
  long $00_00_40_00
  long $00_40_00_00
  long $00_40_40_40

BLANKGREEN
  long $00_02_00_00

BLANKPIX
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0