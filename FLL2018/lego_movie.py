from pixel_hat import HatFrame

bricks = [
    [ 5,1,  2,2],
    [11,1,  4,2],
    [ 1,2,  2,3],
    [ 7,2,  2,1],
    [ 2,4,  4,4],
    [-2,5,  4,5],
    [ 8,6,  4,2],
    [ 4,8,  4,1],
    [11,9,  4,3],
    [-1,10, 2,2],
    [ 8,10, 2,5],
    [ 9,12, 4,4],
    [ 3,12, 2,3],
    [-2,13, 4,1],
    [7,14,  2,2],
    
    [-2,20, 4,5],
    [ 2,20, 4,6],
    [ 6,20, 4,5],
    [10,20, 4,6],    
    [ 0,21, 4,5],
    [ 4,21, 4,6],
    [ 8,21, 4,5],
    [12,21, 4,5]   
]

for brick in bricks:
    brick[0] *= 4
    brick[1] *= 4

pattern = '''
................
.....22....2222.
.33....11.......
................
..4444..........
55............55
........2222....
................
....1111........ 
...........3333.  
2.......55.....2    
................   
...33....4444... 
11............11 
.......22....... 
................
................
................
................
................
5566665555666655
5555666655556666
'''

frag = '''
.**.
****
****
****
****
'''

frag = frag.replace('\n','')

numRows = 22

with open('legoGEN.txt','w') as ps:
    changed = True
    
    ofs = numRows*4-24
    while changed:
        changed = False
        frame = HatFrame()
        for x in range(len(bricks)-1,-1,-1):
            brick = bricks[x]
            for z in range(brick[2]):
                for i in range(4):
                    for j in range(4):
                        frame.set_pixel(i+brick[0]+z*4,j+brick[1]-ofs,brick[3])
                frame.set_pixel(brick[0]+z*4+1,brick[1]-1-ofs,brick[3])
                frame.set_pixel(brick[0]+z*4+2,brick[1]-1-ofs,brick[3])
        ps.write('%\n')
        ps.write(frame.to_string()+'\n')
        
        for brick in bricks[0:-8]:
            can_fall = True
            for z in range(brick[2]):                
                if frame.get_pixel(brick[0]+z*4,brick[1]+4-ofs)!=0:                    
                    can_fall = False
            if can_fall:
                brick[1] += 1
                changed = True
