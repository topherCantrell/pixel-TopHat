import SpriteLoader
import HatFrame

sprites = SpriteLoader.SpriteLoader()

ghostMap = ['#', 1, '*', 2]
ghost = sprites.colorSprite("ghostc",ghostMap)

pacMap = ['#', 3]
pac = sprites.colorSprite("pac2", pacMap)

f = HatFrame.HatFrame()

f.draw_sprite(32-15+32, 1, ghost)  
f.draw_sprite(32+1+32,2,pac)


f.set_ring(0, 4)
f.set_ring(1, 5)
f.set_ring(2, 4)
f.set_ring(3, 5)
f.set_ring(4, 4)
f.set_ring(5, 5)
f.set_ring(6, 4)
f.set_ring(7, 5)
f.set_ring(8, 4)
f.set_ring(9, 5)
f.set_ring(10, 4)
f.set_ring(11, 5)

f.set_ring(28, 4)
f.set_ring(29, 5)
f.set_ring(30, 4)
f.set_ring(31, 5)
f.set_ring(32, 4)
f.set_ring(33, 5)
f.set_ring(34, 4)
f.set_ring(35, 5)

with open("stillGEN.txt","w") as ps:
    ps.write(f.to_string()+"\n")
    