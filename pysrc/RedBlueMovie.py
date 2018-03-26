import SpriteLoader
import HatFrame

sprites = SpriteLoader.SpriteLoader()

letterMap = ['#', 1]

letterG = sprites.colorSprite("letterG", letterMap)
lettero = sprites.colorSprite("lettero", letterMap)
                
five = sprites.colorSprite("five", letterMap)
eight = sprites.colorSprite("eight", letterMap)

with open("redBlueGEN.txt","w") as ps:
    for i in range(0,10):
        for x in range(0,63,2):
            f = HatFrame.HatFrame()
            f.draw_sprite(x+0,2+1,letterG)
            f.draw_sprite(x+13, 2+5, lettero)
            f.draw_sprite(x+23, 2+0, five)
            f.draw_sprite(x+33, 2+0, eight)
            f.draw_sprite(x+43, 2+0, five)
            f.draw_sprite(x+53, 2+0, eight)
            
            ps.write("%\n")
            ps.write(f.to_string()+"\n")
    
    ps.write("\n")        