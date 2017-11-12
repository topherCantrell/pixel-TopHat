# PixelHat

A top hat covered in NEO pixels for the 2017/2018 FIRST Robotics season.

Thanks to Gary Dion (http://garydion.com/). He helped  design the pixel layout,
and he found all of the Neo Pixels on eBay. He also found the 5V DC converter 
at Digikey.

# Parts

Four flexible grids for the body. $148<br>
http://www.ebay.com/itm/282616038722

One pixel circle for the top. $48<br>
http://www.ebay.com/itm/311923131692

Six meters of 144/m strips for the brim and fill for the top. $100.80<br>
http://www.ebay.com/itm/222533276234

One DC/DC converter from Digikey. $36<br>
https://www.digikey.com/product-detail/en/delta-electronics/E36SC05025NRFA/941-1638-ND/3995553

Two 24V batteries from Lowe's. $20<br>
https://www.lowes.com/pd/Kobalt-24-Volt-1-5-Amp-Hours-Lithium-Power-Tool-Battery/1000090833

One Kobalt battery charger from Lowe's. $40<br>
https://www.lowes.com/pd/Kobalt-24-Volt-Max-Power-Tool-Battery-Charger/1000102901

One foam pad from Amazon. $13<br>
https://www.amazon.com/gp/product/B00069PFKK/ref=oh_aui_detailpage_o05_s00

Eight 1000uF capacitors from DigiKey. $5<br>
https://www.digikey.com/product-detail/en/rubycon/25PX1000MEFCT810X16/1189-1583-1-ND/3134540

Two logic-level converters from Sparkfun. $6<br>
https://www.sparkfun.com/products/12009

Contact cement, wires, etc.

I reused two propeller boards from a previous project:<br>
https://github.com/topherCantrell/snap/blob/master/SnapMidi/hardware/SnapMusic.sch<br>
https://github.com/topherCantrell/snap/blob/master/SnapMidi/hardware/SnapMusic.pcb<br>

# Power

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/power.jpg">

# CPUs

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/cpus.jpg">

# Construction

For the body of the hat I glued the four flexible grids to the foam curving the foam into a 
circle as I went. I cut holes in the foam for the wires to pass through. I glued the edges of 
the foam together to make a circle.

I cut the elliptical top from the foam. I shaped the ellipse to the short axis is the diameter
of the pixel circle. I put the pixel circle in the center and filled the long axis in with
short pixel strips.

The brim uses 64 strips of 9 pixels. 5 pixels stick out from the body, then folded to put 1
pixel on the edge facing out, then folded again with 3 pixels on the bottom. 

# Circuit

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/schematic1.jpg">

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/schematic2.jpg">

# Animation Sequences

## Pacman
  - Line of all 4 ghosts chase Pacman around the brim a couple of times
  - They get closer and closer
  - A power pill appears
  - Pacman eats it, they turn blue, and he truns to chase them eating them one by one
  - The scores fly around the hat behind him
  - They start flashing. Before he can eat the last one it changes.
  - The ghost disappears and pacman dies.
  
## Mario
  - Mario from Donkey Kong runs around the hat. There is no room for him to jump.
  
## QBert
  - Qbert stands on the side of the hat
  - A pacman ghost bumps into him and runs off
  - Qbert spews his swear line
  
## Space Invaders
  - Two lines of space invaders march around the hat
  - The bottom row is shot out one by one
  - The top row advances down
  - The flying saucer flashes around the top line

## Sprites

http://simonowen.com/sam/articles/pacemu/

