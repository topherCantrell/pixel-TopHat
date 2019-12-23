from test.test_getargs2 import ComplexSubclass2

# 1+ White
# 2# Red
skate_colors = {'.':0,'+':1,'#':2}
skate = ['''
+++......
++#++....
++++#++#.
+++++++++
#########
#.#...#.#
.#.....#.
#.#...#.#
''','''
+++......
++#++....
++++#++#.
+++++++++
#########
.#.....#.
###...###
.#.....#.    
''','''
+++......
++#++....
++++#++#.
+++++++++
#########
#.#...#.#
.#.....#.
#.#...#.#
''','''
+++......
++#++....
++++#++#.
+++++++++
#########
.#.....#.
###...###
.#.....#.   
''']

# 3$ Blue
# 4% Red
# 5@ White
yoyo_colors = {'.':0, '$':3, '%':4, '@':5}
yoyo= ['''
..$$$.@
.$$$$@.
$$$$%$$
$$$%$$$
$$%$$$$
.%$$$$.
..$$$..
''','''
..$$$.@
.$$$$@.
$$$$$$$
%%%%%%%
$$$$$$$
.$$$$$.
..$$$..
''','''
..$$$.@
.%$$$@.
$$%$$$$
$$$%$$$
$$$$%$$
.$$$$%.
..$$$..
''','''
..$%$.@
.$$%$@.
$$$%$$$
$$$%$$$
$$$%$$$
.$$%$$.
..$%$..
''']

# 6+ Green
# 7# Brown
# 8@ Blue
# 9$ White
# 10% Red
tree_colors = {'.':0, '+':6, '#':7, '@':8, '$':9, '%':10}
tree = ['''
.......%%.......
.....++@+++.....
...+++++$++++...
.....%+++++.....
...$+++++%+++...
.++$+++++++++++.
....+++$++++....
..+++%+++++@++..
.+++++++++%++++.
++$+++@++++++%++
.......##.......
.......##.......
''','''
.......$+.......
.....++@+++.....
...++%+++@@++...
.....+%+$$+.....
...+$++++%++@...
.+++++$++++++%+.
....++++@+++....
..++@+++%+++%+..
.++$+++@+++++%+.
+++$+++%++++@+++
.......##.......
.......##.......
''','''
.......+@.......
.....$++++@.....
...%+++$+++++...
.....++@+++.....
...++%+++$+++...
.++++%++++$++$+.
....++@+++++....
..+@+++%++++$+..
.++++%+++$+++++.
++++@+++%+$++++%
.......##.......
.......##.......
''','''
.......+%.......
.....++$++@+.....
...++%++@++++...
.....+++$+++.....
...+++%+++@++...
.++++++$+++@+++.
....$++++%++....
..++$+%++++++@+..
.+++++$++++++++.
$+++++$+++%++++@
.......##.......
.......##.......
''']

from SpriteLoader import Sprite
from pixel_hat import HatFrame

data = {}
s1 = Sprite(skate,0,6,0,skate_colors,flip_horz=True)
data[s1] = [1,0,8]
y1 = Sprite(yoyo,9,5,2,yoyo_colors)
data[y1] = [-1,0,10]
t1 = Sprite(tree,16,4,0,tree_colors)

y2 = Sprite(yoyo,37,0,0,yoyo_colors,flip_horz=True)
data[y2] = [-1,0,8]
s2 = Sprite(skate,33,6,1,skate_colors)
data[s2] = [1,33,38]
t2 = Sprite(tree,48,4,2,tree_colors,flip_horz=True)

def move_skate(s):
    s.num += 1
    if s.num == 4:
        s.num = 0
        
    dat = data[s]
    s.x += dat[0]
    if s.x<dat[1]:
        s.x = dat[1]+2
        dat[0] = 1
    if s.x>dat[2]:
        s.x = dat[2]-2
        dat[0] = -1

def move_yoyo(y):
    y.num += 1
    if y.num == 4:
        y.num = 0
        
    dat = data[y]
    y.y += dat[0]
    if y.y<dat[1]:
        y.y = dat[1]+2
        dat[0] = 1
    if y.y>dat[2]:
        y.y = dat[2]-2
        dat[0] = -1

def move_tree(t):
    t.num += 1
    if t.num == 4:
        t.num = 0

    
with open('toysGEN.txt','w') as ps:

    for _ in range(32):

        frame = HatFrame()
        s1.draw_image(frame)
        #y1.draw_image(frame)
        t1.draw_image(frame)
        y2.draw_image(frame)
        #s2.draw_image(frame)
        t2.draw_image(frame)    
        #for y in range(y1.y):
        #    frame.set_pixel(y1.x+6,y,5)
        for y in range(y2.y):
            frame.set_pixel(y2.x,y,5)
            
        ps.write(frame.to_string())
            
        move_skate(s1)
        move_skate(s2)
        move_yoyo(y1)
        move_yoyo(y2)
        move_tree(t1)
        move_tree(t2)


