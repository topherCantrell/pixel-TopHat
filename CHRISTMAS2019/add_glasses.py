'''

Each lens is 24 pixels.

Pixels are numbered clockwise facing the lens.

The left eye is is 0-23 with 1 at the top.

The right eye is 24-47 with 47 at the top.

'''

import random

def make_solid(num_frames,color):
    ret = []
    for i in range(num_frames):        
        fr = [color]*48
        ret.append(fr)        
    return ret

def make_random(num_frames,first_color,second_color):
    ret = []
    for i in range(num_frames):
        fr = []
        for j in range(48):
            fr.append(random.randint(first_color,second_color))
        ret.append(fr)        
    return ret

def make_spin(num_frames,buffer,left_cw=False,right_cw=True):
    ret = []
    pos = 0
    for i in range(num_frames):
        fr = []
        for k in range(2):
            ofs = pos
            for i in range(24):
                if ofs==24:
                    ofs = 0
                fr.append(buffer[ofs])
                ofs += 1
            pos = pos + 1
            if pos==24:
                pos = 0
        ret.append(fr)
    return ret

#

def load_movie(name):
    with open(name) as f:
        movie_txt = f.readlines()    
        
    num_frames = 0
    for t in movie_txt:
        if t.startswith('%'):
            num_frames += 1
        
    return movie_txt,num_frames
    
def save_new_movie(name,txt):
    with open(name,'w') as f:
        f.writelines(txt)
        
def merge_eyes(movie_txt,eye_data):
    ptr = 0
    for data in eye_data:
        while not movie_txt[ptr].startswith('%'):
            ptr+=1
        ptr += 33
        dp = 0
        r = 0
        c = 0
        rcnt = 0
        rdir = 1   
        for i in data:
            t = hex(i).upper()[2:]
            if len(t)<2:
                t = '0'+t                     
            g = movie_txt[ptr+r]
            g = g[0:int(c*3)] + t + ' '+g[int((c+1)*3):]
            movie_txt[ptr+r] = g         
            
            g = movie_txt[ptr+r]
            g = g[0:int((c+32)*3)+2] + t + ' '+g[int((c+33)*3)+2:]
            movie_txt[ptr+r] = g 
            
            r = r + rdir
            if r==8:
                r = 7
                c = c + 1
                rdir = -rdir
            if r==-1:
                r = 0
                c = c + 1
                rdir = -rdir
            
    # Frame by frame: replace brim with eye data
    pass            
    
#
# snow.txt
#
movie_txt,num_frames = load_movie('snow.txt')
eye_data = make_random(num_frames,0,6)
merge_eyes(movie_txt,eye_data)
save_new_movie('snow_eyes.txt',movie_txt)

#
# sparkle.txt
#
# Leave this as is

#
# merry.txt
#
movie_txt,num_frames = load_movie('merry.txt')
eye_data = make_spin(num_frames,[1,1,2,2,2,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(eye_data)
merge_eyes(movie_txt,eye_data)
save_new_movie('merry_eyes.txt',movie_txt)

#
# orbit.txt
#
movie_txt,num_frames = load_movie('orbit.txt')
eye_data = make_spin(num_frames,[42,0,0,0, 35,0,0,0, 28,0,0,0, 21,0,0,0, 14,0,0,0, 7,0,0,0,0])
merge_eyes(movie_txt,eye_data)
save_new_movie('orbit_eyes.txt',movie_txt)


#
# toys.txt
#
movie_txt,num_frames = load_movie('toys.txt')
eye_data = make_random(num_frames,0,10)
merge_eyes(movie_txt,eye_data)
save_new_movie('toys_eyes.txt',movie_txt)


#
# pacman.txt
#
movie_txt,num_frames = load_movie('pacman.txt')
eye_data = make_random(num_frames,0,14)
merge_eyes(movie_txt,eye_data)
save_new_movie('pacman_eyes.txt',movie_txt)








