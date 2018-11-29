from SpriteLoader import SpriteLoader
from pixel_hat import HatFrame

sprites = SpriteLoader() # Contains all the sprite ASCII art

invaderMap = ['#', 1] # Maps of ASCII characters to color numbers
invaders = [ 
    sprites.doubler(sprites.colorSprite("invaderB1", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderB2", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderC1", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderC2", invaderMap))
    ]

with open("invGEN.txt","w") as ps:
    
    for y in range(-15,0,1):    
        f = HatFrame()
        ofs = abs(y%2) 
        f.draw_sprite(0, y, invaders[ofs])    
        f.draw_sprite(35,y, invaders[2+ofs])
        ps.write(f.to_string())

    
    for x in range(64):
        f = HatFrame()
        ofs = abs(x%2) # Every step alternate sprite images       
        f.draw_sprite(x+0, 0, invaders[ofs]);    
        f.draw_sprite(x+35,0, invaders[2+ofs]);
        ps.write(f.to_string())
       
    for y in range(0,-16,-1):
        f = HatFrame()
        ofs = abs(y%2) 
        f.draw_sprite(0, y, invaders[ofs]);    
        f.draw_sprite(35,y, invaders[2+ofs]);
        ps.write(f.to_string())
        