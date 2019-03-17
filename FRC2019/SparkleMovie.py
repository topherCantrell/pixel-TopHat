from pixel_hat import HatFrame
import random

# 1831 possible
# Ten frames per second
# Twenty seconds = 200 frames
        
# 8 fade on
# 8 hold
# 8 fade out
        
# 300 pixel events

pixels = []
for x in range(200):
    r = []
    for y in range(1831):
        r.append(0)
    pixels.append(r)

for z in range(2000):
    while True:
        color = random.randint(0,6)+1
        pix = random.randint(0,1830)
        sf = random.randint(0,200-24-1)
        
        ok = True
        for g in range(sf,sf+24):  
            if pixels[g][pix]!=0:
                ok = False
                break
        if not ok:
            continue
        
        for g in range(8):
            pixels[sf+g][pix] = color*8+(7-g)+1 # Fade in
        for g in range(8):
            pixels[sf+g+8][pix] = color*8+1 # Hold
        for g in range(8):
            pixels[sf+g+16][pix] = color*8+g+1 # Fade on
        break
    
with open("sparkGEN.txt","w") as ps:
    for pix in pixels:
        f = HatFrame()
        for p in range(1831):
            if pix[p]!=0:
                f.set_raw_pixel(p,pix[p])
        ps.write(f.to_string())
    

