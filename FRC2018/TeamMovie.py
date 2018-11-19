import SpriteLoader
import HatFrame

sprites = SpriteLoader.SpriteLoader()

ghostMap = ['#', 1, '*', 2, '+', 3]
letterMap = ['#', 4]
                     
ghostA = sprites.colorSprite("ghosta", ghostMap)
ghostB = sprites.colorSprite("ghostb", ghostMap)

five = sprites.colorSprite("five", letterMap)
eight = sprites.colorSprite("eight", letterMap)

with open("teamGEN.txt","w") as ps:
    
    for y in range(22,1,-1):
        f = HatFrame.HatFrame()
        if (y%2)==0:
            f.draw_sprite(0,  y+1, ghostA)
        else:
            f.draw_sprite(0,  y+1, ghostB)
        
        f.draw_sprite(18, y+2, five)
        f.draw_sprite(28, y+2, eight)
        f.draw_sprite(38, y+2, five)
        f.draw_sprite(48, y+2, eight)
        ps.write("%\n")
        ps.write(f.to_string()+"\n")
    
     
    for z in range(2):
        for x in range(63):
            f = HatFrame.HatFrame()
            if (x%2)==0:
                f.draw_sprite(x+0,  1, ghostA)
            else:
                f.draw_sprite(x+0,  1, ghostB)
            
            f.draw_sprite(x+18, 2, five)
            f.draw_sprite(x+28, 2, eight)
            f.draw_sprite(x+38, 2, five)
            f.draw_sprite(x+48, 2, eight)
            ps.write("%\n")
            ps.write(f.to_string()+"\n")
            
    for y in range(1,23):
        f = HatFrame.HatFrame()
        if (y%2)==0:
            f.draw_sprite(0,  y+1, ghostA)
        else:
            f.draw_sprite(0,  y+1, ghostB)
        f.draw_sprite(18, y+2, five)
        f.draw_sprite(28, y+2, eight)
        f.draw_sprite(38, y+2, five)
        f.draw_sprite(48, y+2, eight)
        ps.write("%\n")
        ps.write(f.to_string()+"\n")
            