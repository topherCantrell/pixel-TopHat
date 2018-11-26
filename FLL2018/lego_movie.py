from HatFrame import HatFrame

bricks = [
    [ 5,1,  2,2],
    [11,2,  4,2],
    [ 1,3,  2,3],
    [ 7,3,  2,1],
    [ 2,4,  4,4],
    [-2,5,  4,5],
    
]

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
.........4444...
...33...........
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

pattern = pattern.replace('\n','')
frag = frag.replace('\n','')

numRows = int(len(pattern)/16)*4

buffer = []
for i in range(numRows):
    buffer.append([0]*(16*4))

for i in range(len(pattern)):    
    y = int(i/16)*4
    x = int(i%16)*4
    for yy in range(4):
        for xx in range(4):
            buffer[y+yy][x+xx] = pattern[i]
    if y>0 and pattern[i]!='.' and buffer[y-1][x+1]=='.':
        buffer[y-1][x+1] = pattern[i]
        buffer[y-1][x+2] = pattern[i]            
            
with open("legoGEN.txt","w") as ps:
    
    for _ in range(60):            
        frame = HatFrame()
        for y in range(24):
            for x in range(64):
                c = buffer[y+numRows-24][x]
                if c=='.':
                    c=0
                else:
                    c=int(c)
                frame.set_pixel(x,y,c)
        ps.write("%\n")
        ps.write(frame.to_string()+"\n")
        # Collapse 1 row
        
        # 4 columns at a time. Find the first blank from the bottom. Close down from
        # there up
        
        for xx in range(0,64,4):
            yy = numRows-9
            while buffer[yy][xx]!='.':
                yy = yy - 1
            if buffer[yy-1][xx]=='.':
                yy = yy - 1
            for i in range(4):
                j = yy
                while j>0:
                    buffer[j][xx+i] = buffer[j-1][xx+i]
                    j = j -1

