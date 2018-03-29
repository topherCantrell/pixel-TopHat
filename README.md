# PixelHat

A top hat covered in NEO pixels for the 2017/2018 FIRST Robotics season.

Much thanks to my buddy Gary Dion for suggestions and support.

On AdaFruit Show-and-Tell: https://youtu.be/zwyWCEgpvOA?t=411

# Parts

Four flexible grids for the body. $148<br>
http://www.ebay.com/itm/282616038722<br>
From adafruit: https://www.adafruit.com/product/2294

One pixel circle for the top. $48<br>
http://www.ebay.com/itm/311923131692<br>
Amazon: https://www.amazon.com/MOKUNGIT-WS2812B-Ring-RGB-Integrated/dp/B077JY6796

Six meters of 144/m strips for the brim and fill for the top. $100.80<br>
http://www.ebay.com/itm/222533276234
From adafruit: https://www.adafruit.com/product/1506

One DC/DC converter from Digikey. $36<br>
https://www.digikey.com/product-detail/en/delta-electronics/E36SC05025NRFA/941-1638-ND/3995553

Two 24V batteries from Lowe's. $20<br>
https://www.lowes.com/pd/Kobalt-24-Volt-1-5-Amp-Hours-Lithium-Power-Tool-Battery/1000090833

One Kobalt battery charger from Lowe's. $40<br>
https://www.lowes.com/pd/Kobalt-24-Volt-Max-Power-Tool-Battery-Charger/1000102901

One foam pad from Amazon. $13<br>
https://www.amazon.com/gp/product/B00069PFKK

Eight 1000uF capacitors from DigiKey. $5<br>
https://www.digikey.com/product-detail/en/rubycon/25PX1000MEFCT810X16/1189-1583-1-ND/3134540

Two logic-level converters from Sparkfun. $6<br>
https://www.sparkfun.com/products/12009

Pi Zero W from adafruit. $10<br>
https://www.adafruit.com/product/3400

Adhesive felt sheets from Amazon. $10<br>
https://www.amazon.com/gp/product/B076P51CHW/ref=oh_aui_detailpage_o00_s00

Contact cement, wires, etc.

I reused two propeller boards from a previous project:<br>
https://github.com/topherCantrell/snap/blob/master/SnapMidi/hardware/SnapMusic.sch<br>
https://github.com/topherCantrell/snap/blob/master/SnapMidi/hardware/SnapMusic.pcb<br>

# Construction

[CONSTRUCTION.md](CONSTRUCTION.md)

For the body of the hat I glued the four flexible grids to the foam curving the foam into a 
circle as I went. I cut holes in the foam for the wires to pass through. I glued the edges of 
the foam together to make a cylinder.

I cut the elliptical top from the foam. I shaped the ellipse so that the short axis is the diameter
of the pixel circle. I put the pixel circle in the center and filled the long axis in with
short pixel strips.

The brim uses 64 strips of 8 pixels. 4 pixels stick out from the body, then folded to put 1
pixel on the edge facing out, then folded again with 3 pixels on the bottom. 

# Circuit

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/figure4.png">

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/figure3.png">

# Web Interface

The Pi Zero is configured as an access point. You connect to it with your phone and load the control page.

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/web.jpg">

# SD Card Format

Each animation sequence begins with a three-sector (1536 bytes) descriptor:
  - First Sector
    - Number of frames (4 bytes)
    - Frames per second (4 bytes)
  - Second and Third Sector
    - Color map of 256 colors 256*4 = 1024 bytes
  
The first sector of the file is a map of the animations. It is a list of 16-byte entries. An entry that
starts with a 0 ends the list.
  - Name (null terminated fixed 12 bytes)
  - Starting sector (4 bytes)

# Software

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/figure6.png">

<img src="https://github.com/topherCantrell/pixelHat/blob/master/art/figure7.png">
