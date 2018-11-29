from pixel_hat import HatFrame

with open('color_test.txt','w') as ps:
    
    frame = HatFrame()
    
    for y in range(7):
        for x in range(16):
            color = y*16 + x            
            frame.set_pixel(x*3,y*3,color)
            frame.set_pixel(x*3+1,y*3,color)
            frame.set_pixel(x*3,y*3+1,color)
            frame.set_pixel(x*3+1,y*3+1,color)    
    
    ps.write(frame.to_string())