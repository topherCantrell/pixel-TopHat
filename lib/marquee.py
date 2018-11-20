import draw_text

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

class HatFrameAdapter:
    
    def __init__(self,frame,loop):
        self._frame = frame
        self._loop = loop
        
    def set_side_brim_pixel(self,x,y,color):
        nx = self._loop.trans(x)
        if nx!=None:
            frame.set_side_brim_pixel(nx,y,color)
    
class Marquee:
    
    # Options:
    # Appear on or scroll on
    # Loop or exit
    # Make 3x buffer for on and off as needed
    
    def __init__(self,y,text,font,color,letter_offset=1,
                 phys_ofs=0,length=None,view_start=0,view_length=64):
        if length==None:
            length = draw_text.get_string_length(text,font,letter_offset)+letter_offset
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
        # True makes a double buffer
        # False makes a single buffer
        # To scroll on, set the pos to the start of the second half and advance backwards
        # To scroll off, continue to advance backwards
        # To loop scroll, set the single buffer
        if enable:
            self._loop = Loop(self._length*2,self._view_start,self._view_length,self._phys_ofs)
        else:
            self._loop = Loop(self._length,self._view_start,self._view_length,self._phys_ofs)
        
    def draw(self,frame):
        adapt = HatFrameAdapter(frame,self._loop)
        draw_text.draw_string(self._font,adapt,self._pos,self._y,self._text,self._color,self._letter_offset)
    
    def scroll(self,ofs):
        self._pos += ofs
    
    
from HatFrame import HatFrame

marquee = Marquee(12,'Stacy','FreeSerif9pt7b',1,0)
#marquee = Marquee(12,64,0,64,0,'Testing','FreeSerif9pt7b',1)
                  
frame = HatFrame()

marquee.scroll(-15)
marquee.draw(frame)

print(frame.to_string())

import dev
dev.show_frame(frame)
