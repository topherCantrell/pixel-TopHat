from SpriteLoader import SpriteLoader
from HatFrame import HatFrame

sprites = SpriteLoader() # Contains all the sprite ASCII art

invaderMap = ['#', 1] # Maps of ASCII characters to color numbers
invaders = [ 
    sprites.doubler(sprites.colorSprite("invaderA1", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderA2", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderB1", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderB2", invaderMap))
    ]

with open("invGEN.txt","w") as ps:
        
    for x in range(64):
        f = HatFrame()
        ofs = abs(x%2) # Every step alternate sprite images       
        f.draw_sprite(x+0, 0, invaders[ofs]);    
        f.draw_sprite(x+35,0, invaders[2+ofs]);
        ps.write("%\n") # Mark between frames
        ps.write(f.to_string()+"\n")
