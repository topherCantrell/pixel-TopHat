CON
  _clkmode        = xtal1 + pll16x
  _xinfreq        = 5_000_000

CON    
    pinS1   = 19
    pinS2   = 20
    pinS3   = 21
    pinS4   = 22
    '
    pinCS   = 24
    pinDI   = 25
    pinSCLK = 26
    pinDO   = 27 

OBJ    
    STRIPA   : "NeoPixelStrip"
    STRIPB   : "NeoPixelStrip"
    STRIPC   : "NeoPixelStrip"
    STRIPD   : "NeoPixelStrip"
    '
    PST      : "Parallax Serial Terminal"
    SD       : "SDCard"      

VAR
    byte animationMap[512]    
    byte movieConfig[512]    
    byte colorPalette[1024]
    byte adjustedColors[1024]
    byte frameBuffer[1024*2]
    
    long currentFrameCount
    long currentSector
    long currentDelay

    long bufferOffset
    long bufferNextOffset

PUB Main | i

  ' Drive the pixel data lines low
  outa[pinS1] := 0
  dira[pinS1] := 1
  outa[pinS2] := 0
  dira[pinS2] := 1
  outa[pinS3] := 0
  dira[pinS3] := 1
  outa[pinS4] := 0
  dira[pinS4] := 1  

  ' frameBuffer used for scratch during the startup process
  SD.start(@frameBuffer, pinDO, pinSCLK, pinDI, pinCS)
  
  PauseMSec(2000) ' For development ... give time to switch to terminal   
  PST.start(115200)

  SD.readFileSectors(@animationMap,0,1)
  SD.waitForDone     

  ' First animation
  currentSector := 1

  repeat  
    
    SD.waitForDone ' We might be in the middle of a cache operation from below

    ' Read the info on the movie   
    SD.readFileSectors(@movieConfig,currentSector,1)
    SD.waitForDone ' We need this info
    
    currentFrameCount := long[@movieConfig]
    currentDelay := long[@movieConfig+4]

    if currentFrameCount == 0
      ' End of all animations -- restart at the beginning of the disk
      currentSector := 1      
      next

    ' Read the color palette
    SD.readFileSectors(@colorPalette,currentSector+1,2)
    SD.waitForDone ' We need this info

    ' Skip to first frame
    currentSector := currentSector + 3

    ' Current and back buffer
    bufferOffset := 0
    bufferNextOffset := 1024

    ' Read the first frame. We have to wait on this one.
    SD.readFileSectors(@frameBuffer,currentSector,2)
    SD.waitForDone 

    repeat

      ' Check for serial command
      if PST.RxCount > 0
        PST.StrIn(@movieConfig)
        ' TODO handle brightness command

        ' Start on new animation
        currentSector := getAnimationSector
        quit
      
      ' Start loading the next frame in the back buffer
      SD.waitForDone ' Hopefully this never waits (long delay coming up)          
      SD.readFileSectors(@frameBuffer+bufferNextOffset,currentSector,2)

      ' Next sector to use
      currentSector := currentSector + 2   

      ' Draw the current frame
      STRIPA.draw(2, @colorPalette, @frameBuffer    +bufferNextOffset, pinS1, 256)
      STRIPB.draw(2, @colorPalette, @frameBuffer+256+bufferNextOffset, pinS2, 256)
      STRIPC.draw(2, @colorPalette, @frameBuffer+512+bufferNextOffset, pinS3, 256)
      STRIPD.draw(2, @colorPalette, @frameBuffer+768+bufferNextOffset, pinS4, 256)

      ' Now for a long delay between frames (the SD should complete here)
      PauseMSec(currentDelay)

      ' Count the frames      
      currentFrameCount := currentFrameCount - 1
      if currentFrameCount == 0
        ' End of this sequence -- break out to load next sequence        
        quit

      ' Swap the back buffer and the current buffer
      i := bufferOffset
      bufferOffset := bufferNextOffset
      bufferNextOffset := i

' Compare two strings. Return 1 if the same or 0 if not
PRI strCmp(a,b)
  repeat
    if byte[a] <> byte[b]
      return 0
    if byte[a] == 0
      return 1
    a := a+1
    b := b+1    

' Find the entry in the animation map. Return the info sector (or 1 if not found)    
PRI getAnimationSector | i
  i := 0 ' First entry in table                         
  repeat
    if byte[@animationMap+i] == 0
      return 1 ' Couldn't find it ... go back to the first
    if strCmp(@animationMap+i,@movieConfig)==1
      return long[@animationMap+i+12]
    i := i + 16 ' Next entry  
     
PRI PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)
