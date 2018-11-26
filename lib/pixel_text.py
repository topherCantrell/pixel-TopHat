import importlib

# 8x9
# https://fontstruct.com/fontstructions/show/1208100/16-bit-7x9-nostalgia

# 5x7
# https://www.123rf.com/photo_57003905_stock-vector-pixel-font-set-of-letters.html
# https://www.bigstockphoto.com/image-95284172/stock-vector-8-bit-font

def draw_char(font,frame,x,y,c,color):
            
    c = ord(c) - 0x20    
    offs,width,height,adv_cursor,x_ofs,y_ofs = font.Glyphs[c]
    
    num_bytes = int(width*height/8)+1
    
    s = ''
    for i in range(num_bytes):
        s = s + '{:08b}'.format(font.Bitmaps[offs+i])
        
    for j in range(height):
        for i in range(width):
            c = s[j*width+i]
            if c == '1':
                c = color
                nx = x+x_ofs+i
                frame.set_pixel(nx, y+y_ofs+j, color)
    return adv_cursor

def get_string_length(s,font,letter_offset=1):
    font = importlib.import_module('pixel_text_fonts.'+font)
    ret = 0
    for c in s:
        c = ord(c) - 0x20 
        ret = ret + font.Glyphs[c][3] + letter_offset
    return ret
     
def draw_string(font,frame,x,y,s,color,letter_offset=1):
    font = importlib.import_module('pixel_text_fonts.'+font)
    if not isinstance(color,list):
        color = [color]
    cp = 0    
    for c in s:
        x += draw_char(font,frame,x,y,c,color[cp])
        x += letter_offset
        cp = cp + 1
        if cp>=len(color):
            cp = 0
    return x        

class Marquee:
    
    def __init__(self,font,s,color,start=0,length=64):
        self._length = length
        self._start = start
        self._font = font
        self._s = s
        self._color = color
        self._pos = self._length+self._start-1
        
    def draw(self,frame,start_bar_color=None,stop_bar_color=None):
        pass
    
    def advance(self,distance):
        pass

