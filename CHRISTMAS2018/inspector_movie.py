import marquee

with open("inspectorGEN.txt","w") as ps:
        
    colors = [1,2,3,4]
    frames = marquee.scroll_on_loop_off(13,'Toy Inspector #7  ', 'FreeSerif9pt7b', colors,1,2)
    
    for frame in frames:
        for y in range(24):
            frame.set_pixel(63,y,3)
        ps.write(frame.to_string())