
class Window:    
    def __init__(self,parent,x,y,width,height):
        self._parent = parent
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    
    def set_pixel(self,x,y,color):
        pass
    
class HatFrameWindowAdapter:
    def __init__(self,frame):
        self._frame = frame
        
    def set_pixel(self,x,y,color):
        self._frame.set_side_brim_pixel(x,y,color)