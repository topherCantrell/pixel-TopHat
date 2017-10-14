CON
  _clkmode        = xtal1 + pll16x
  _xinfreq        = 5_000_000

CON
    PIN_D1 = 0

OBJ    
    STRIP    : "NeoPixelStrip"    
    'PST      : "Parallax Serial Terminal"      

VAR    
    
PUB Main

  ' Go ahead and drive the pixel data lines low.
  dira[PIN_D1] := 1
  outa[PIN_D1] := 0

  STRIP.init

  PauseMSec(1000)

  STRIP.draw(2, @colors, @pixels, PIN_D1, 256)

  repeat
    PauseMSec(5000)
  
      
PRI PauseMSec(Duration)
  waitcnt(((clkfreq / 1_000 * Duration - 3932) #> 381) + cnt)

DAT

colors

    long $00_00_00_00
    long $00_05_05_05      

pixels

    byte 1,1,0,1,1,0,1,0
    byte 0,1,0,0,1,0,1,0    
    byte 0,0,0,0,0,0,0,0
    byte 1,0,0,0,0,0,0,0
    byte 0,1,0,0,0,0,0,0
    byte 0,0,1,0,0,0,0,0
    byte 0,0,0,1,0,0,0,0
    byte 0,0,0,0,1,0,0,0
    byte 0,0,0,0,0,1,0,0
    byte 0,0,0,0,0,0,1,0
    byte 0,0,0,0,0,0,0,1
    byte 0,0,0,0,0,0,1,0
    byte 0,0,0,0,0,1,0,0
    byte 0,0,0,0,1,0,0,0
    byte 0,0,0,1,0,0,0,0
    byte 0,0,1,0,0,0,0,0 
    byte 0,1,0,0,0,0,0,0
    byte 1,0,0,0,0,0,0,0
    byte 0,1,0,0,0,0,0,0
    byte 0,0,1,0,0,0,0,0
    byte 0,0,0,1,0,0,0,0
    byte 0,0,0,0,1,0,0,0
    byte 0,0,0,0,0,1,0,0
    byte 0,0,0,0,0,0,1,0
    byte 0,0,0,0,0,0,0,1
    byte 0,0,0,0,0,0,1,0
    byte 0,0,0,0,0,1,0,0
    byte 0,0,0,0,1,0,0,0
    byte 0,0,0,1,0,0,0,0
    byte 0,0,1,0,0,0,0,0
    byte 0,1,0,0,0,0,0,0
    byte 1,1,0,0,0,1,0,1
    