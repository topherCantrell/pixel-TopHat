# Circuit python
# Tester for pixels

import board
import neopixel
pixels = neopixel.NeoPixel(board.GP28,256)
pixels.fill( (20,20,20) )
