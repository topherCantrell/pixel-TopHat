import SpriteLoader
import HatFrame
from errno import EROFS

sprites = SpriteLoader.SpriteLoader()

invaderMap = ['#', 1]
invaders = [
    sprites.doubler(sprites.colorSprite("invaderA1", invaderMap)),
    sprites.doubler(sprites.colorSprite("invaderA2", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderB1", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderB2", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderC1", invaderMap)),    
    sprites.doubler(sprites.colorSprite("invaderC2", invaderMap))
    ]

with open("invGEN.txt","w") as ps:
    
    for y in range(-15,0,1):    
        f = HatFrame.HatFrame()
        ofs = y%2
        if ofs<0:
             ofs=-ofs
        f.draw_sprite(0, y, invaders[2+ofs])    
        f.draw_sprite(35,y, invaders[4+ofs])
        ps.write("%\n")
        ps.write(f.to_string()+"\n")

    
    for x in range(0,64):
        f = HatFrame.HatFrame()
        ofs = x%2
        if ofs<0:
            ofs=-ofs
        f.draw_sprite(x+0, 0, invaders[2+ofs]);    
        f.draw_sprite(x+35,0, invaders[4+ofs]);
        ps.write("%\n")
        ps.write(f.to_string()+"\n")
       
    for y in range(0,-16,-1):
        f = HatFrame.HatFrame()
        ofs = y%2
        if ofs<0:
            ofs=-ofs
        f.draw_sprite(0, y, invaders[2+ofs]);    
        f.draw_sprite(35,y, invaders[4+ofs]);
        ps.write("%\n")
        ps.write(f.to_string()+"\n")
        