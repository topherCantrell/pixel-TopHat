import marquee

with open("merryGEN.txt","w") as ps:
        
    colors = [1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,2,2,2]
    frames = marquee.scroll_on_loop_off(11,'Merry Christmas!! ', 'FreeSerif9pt7b', colors,1,1)
    
    for frame in frames:
        cpos = 0
        for i in range(2,36,2):
            if i<12 or i>27:
                frame.set_ring(i,cpos)
            cpos +=1
            if cpos==4:
                cpos=0
        for y in range(24):
            frame.set_pixel(63,y,3)
        ps.write(frame.to_string())