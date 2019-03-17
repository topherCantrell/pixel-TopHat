import marquee

# print("FLL 2018")
# print("Into Orbit!")

'''

.**..**.
********
********

'''

with open("deepGEN.txt","w") as ps:
    
    # 4 frames per second
    
    #frames = marquee.scroll_across(13,'FLL 2018', 'FreeSerif9pt7b', [1,2,3])
    colors = [1,2,3,0]+[4,5]*5
    frames = marquee.scroll_on_loop_off(13,'FRC Deep Space', 'FreeSerif9pt7b', colors,1,2)

    
    for frame in frames:
        for y in range(16):
            frame.set_pixel(63,y,7)
        ps.write(frame.to_string())