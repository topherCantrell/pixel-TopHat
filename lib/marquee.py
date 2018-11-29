import pixel_text
import pixel_hat

class Loop:
    

    '''
         -4   0                                                      100
          +---|--------------------------------------------------------| Loop
         vs
          |----------| View
         po                         63
    |-----+-------------------------|  Physical
          6
    '''
    
    def __init__(self, length, view_start, view_length, phys_ofs):
        
        if view_length>length:
            raise Exception('View must fit in loop')
        
        self._length = length
        
        self._map = {}
                                
        for i in range(view_length):
            j = view_start + i
            self._map[self._wrap(j)] = j-view_start       
        
        self._phys_ofs = phys_ofs
        
    def _wrap(self,x):
        while x<0:
            x = x + self._length
        while x>=self._length:
            x = x - self._length
        return x
        
    def trans(self,x):
        x = self._wrap(x)
        if x in self._map:
            return self._map[x]+self._phys_ofs
        return None        

class MarqueeGraphics:
    
    def __init__(self,frame,loop):
        self._frame = frame
        self._loop = loop
        
    def set_pixel(self,x,y,color):
        nx = self._loop.trans(x)
        if nx!=None:
            self._frame.set_pixel(nx,y,color)
    
class Marquee:
    
    # TODO explain how to scroll on, off, and loop
    
    def __init__(self,y,text,font,color,letter_offset=1,
                 phys_ofs=0,length=None,view_start=0,view_length=64):
        
        self._view_start = view_start
        self._view_length = view_length
        self._phys_ofs = phys_ofs
        
        if length==None:
            length = pixel_text.get_string_length(text,font,letter_offset)+letter_offset
            if length<64:
                length = 64
        
        self.length = length
                
        self._loop = Loop(length,view_start,view_length,phys_ofs)
        self._y = y
        self._letter_offset = letter_offset
        self._text = text
        self._font = font
        self._color = color
        self._pos = 0
        
    def enable_offscreen(self,enable):       
        if enable:
            self._loop = Loop(self.length*2,self._view_start,self._view_length,self._phys_ofs)
        else:
            self._loop = Loop(self.length,self._view_start,self._view_length,self._phys_ofs)
        
    def draw(self,frame):
        adapt = MarqueeGraphics(frame,self._loop)
        pixel_text.draw_string(self._font,adapt,self._pos,self._y,self._text,self._color,self._letter_offset)
    
    def scroll(self,ofs):
        self._pos += ofs
        
    def set_pos(self,pos):
        self._pos = pos
        
def scroll_across(y,s,font,colors,rate=4):
    ret = []
    mar = Marquee(y,s,font,colors)
    mar.enable_offscreen(True)
    slen = pixel_text.get_string_length(s,font)    
    rate = 0-rate
    for pos in range(64,0-slen,rate):
        mar.set_pos(pos)
        frame = pixel_hat.HatFrame()
        ret.append(frame)            
        mar.draw(frame)
    return ret

def scroll_on_loop_off(y,s,font,colors,loops,rate=4):
    ret = []
    mar = Marquee(y,s,font,colors)
    mar.enable_offscreen(True)
    slen = pixel_text.get_string_length(s,font)    
    rate = 0-rate
    # Scroll on
    for pos in range(64,64-slen,rate):
        mar.set_pos(pos)
        frame = pixel_hat.HatFrame()
        ret.append(frame)            
        mar.draw(frame)
    # Loops
    mar.enable_offscreen(False)
    pos = pos + rate
    for _ in range(int(slen*loops/(1.0-rate))):
        mar.set_pos(pos)
        frame = pixel_hat.HatFrame()
        ret.append(frame)            
        mar.draw(frame)
        pos = pos + rate
    # Scroll off
    pos = pos + rate
    mar.enable_offscreen(True)
    for _ in range(slen-64):
        mar.set_pos(pos+slen)
        frame = pixel_hat.HatFrame()
        ret.append(frame)            
        mar.draw(frame)   
        pos = pos + rate 
        
    return ret