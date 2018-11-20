import SpriteLoader
import HatFrame
import random

sprites = SpriteLoader.SpriteLoader()

def set_rings(f):
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
    
pacPos = -1
def get_pac_image_name():
    global pacPos
    pacPos += 1
    pacPos %= 4
    if pacPos==0:
        return "pac3"
    elif pacPos==1:
        return "pac2"
    elif pacPos==2:
        return "pac1"
    elif pacPos==3:
        return "pac2"
    else:
        return "?"
    
ghostPos = -1
def getBlueGhostImageName():
    global ghostPos
    ghostPos += 1
    ghostPos %= 2
    if ghostPos==0:
        return "ghostc"
    elif ghostPos==1:
        return "ghostd"
    else:
        return "?"
    
def getRedGhostImageName():
    global ghostPos
    ghostPos += 1
    ghostPos %= 2
    if ghostPos==0:
        return "ghosta"
    elif ghostPos==1:
        return "ghostb"
    else:
        return "?"   

def drawFlasher(f,inout,count):
    f.set_pixel(0,7, random.randint(0,2)+12)
    f.set_pixel(0, 8, random.randint(0,2)+12);
    f.set_pixel(1, 7, random.randint(0,2)+12);
    f.set_pixel(1, 8, random.randint(0,2)+12);
    if count>0:
        f.set_pixel(0, 6, random.randint(0,2)+12);
        f.set_pixel(0, 9, random.randint(0,2)+12);
        f.set_pixel(1, 6, random.randint(0,2)+12);
        f.set_pixel(1, 9, random.randint(0,2)+12);
    
    if count>1:
        f.set_pixel(0, 5, random.randint(0,2)+12);
        f.set_pixel(0, 4, random.randint(0,2)+12);
        f.set_pixel(0, 10, random.randint(0,2)+12);
        f.set_pixel(0, 11, random.randint(0,2)+12);
        f.set_pixel(1, 5, random.randint(0,2)+12);
        f.set_pixel(1, 4, random.randint(0,2)+12);
        f.set_pixel(1, 10, random.randint(0,2)+12);
        f.set_pixel(1, 11, random.randint(0,2)+12);
    
    if count>2:
        f.set_pixel(0, 3, random.randint(0,2)+12);
        f.set_pixel(0, 2, random.randint(0,2)+12);
        f.set_pixel(0, 12, random.randint(0,2)+12);
        f.set_pixel(0, 13, random.randint(0,2)+12);
        f.set_pixel(1, 3, random.randint(0,2)+12);
        f.set_pixel(1, 2, random.randint(0,2)+12);
        f.set_pixel(1, 12, random.randint(0,2)+12);
        f.set_pixel(1, 13, random.randint(0,2)+12);
    
    if count>3:
        f.set_pixel(0, 0, random.randint(0,2)+12);
        f.set_pixel(0, 1, random.randint(0,2)+12);
        f.set_pixel(0, 14, random.randint(0,2)+12);
        f.set_pixel(0, 15, random.randint(0,2)+12);
        f.set_pixel(1, 0, random.randint(0,2)+12);
        f.set_pixel(1, 1, random.randint(0,2)+12);
        f.set_pixel(1, 14, random.randint(0,2)+12);
        f.set_pixel(1, 15, random.randint(0,2)+12);
    
    if inout:
        for x in range(2,50-count):
            for y in range(0,16):
                f.set_pixel(x,y,0)
    else:
        for x in range(2,count):
            for y in range(0,16):
                f.set_pixel(x,y,0)
                

sprites = SpriteLoader.SpriteLoader()

blueGhostMap =      ['#', 1, '*', 2]
blueGhostFlashMap = ['#', 6, '*', 7]
redGhostMap =       ['#', 8, '*', 10, '+', 11]    
cyanGhostMap =      ['#', 9, '*', 10, '+', 11]
pacMap =            ['#', 3]
        
with open("pacGEN.txt","w") as ps:
    
    pacX = 32+1+2;
    ghost1X =  32-15+2;
    ghost2X =  ghost1X - 16;        
    
    for i in range(64):
        f = HatFrame.HatFrame()
        set_rings(f)
        f.draw_sprite(pacX, 2, sprites.colorSprite(get_pac_image_name(), pacMap))
        pacX = pacX - 1            
        g = getBlueGhostImageName()
        f.draw_sprite(ghost1X, 1, sprites.colorSprite(g, blueGhostMap))            
        ghost1X = ghost1X - 1
        f.draw_sprite(ghost2X, 1, sprites.colorSprite(g, blueGhostMap))            
        ghost2X = ghost2X - 1
        
        drawFlasher(f,True,i)
        
        ps.write("%\n")
        ps.write(f.to_string()+"\n")
            
    gm = blueGhostMap
    flashTimer = 0
    
    for i in range(64):
        f = HatFrame.HatFrame()
        set_rings(f)
        f.draw_sprite(pacX, 2, sprites.colorSprite(get_pac_image_name(), pacMap))
        pacX = pacX - 1            
        g = getBlueGhostImageName()
        f.draw_sprite(ghost1X, 1, sprites.colorSprite(g, gm))
        ghost1X = ghost1X - 1
        f.draw_sprite(ghost2X, 1, sprites.colorSprite(g, gm))
        ghost2X = ghost2X - 1            
        flashTimer = flashTimer + 1
        if flashTimer == 5:
            if gm==blueGhostMap:
                gm = blueGhostFlashMap
            else:
                gm = blueGhostMap            
            flashTimer = 0
        
        ps.write("%\n")
        ps.write(f.to_string()+"\n")        
    
    for i in range(64):
        f = HatFrame.HatFrame()
        f.draw_sprite(pacX, 2, sprites.flipLeftRight(sprites.colorSprite(get_pac_image_name(), pacMap)))
        pacX = pacX + 1
        g = getRedGhostImageName()
        f.draw_sprite(ghost1X, 1, sprites.colorSprite(g, redGhostMap))
        ghost1X = ghost1X + 1
        f.draw_sprite(ghost2X, 1, sprites.colorSprite(g, cyanGhostMap))
        ghost2X = ghost2X + 1
        
        drawFlasher(f,False,i-8)
        ps.write("%\n")
        ps.write(f.to_string()+"\n")   
        