import marquee

# print("FLL 2018")
# print("Into Orbit!")

'''

.**..**.
********
********

'''

with open("fllGEN.txt","w") as ps:
    
    # 4 frames per second
    
    #frames = marquee.scroll_across(13,'FLL 2018', 'FreeSerif9pt7b', [1,2,3])
    colors = [1,2,3,0,2,2,3,3]+[4,5]*10
    frames = marquee.scroll_on_loop_off(13,'FLL 2018 Into Orbit ', 'FreeSerif9pt7b', colors,1,2)
    
    for frame in frames:
        for y in range(16):
            frame.set_pixel(63,y,7)
        ps.write(frame.to_string())