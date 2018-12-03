
class SignFrame:
           
    def __init__(self,raw=None):
        self._pixels = [0] * (64*32)
        
        if raw != None:              
            raw = raw.replace('%','')
            raw = raw.replace("-", "")
            raw = raw.replace("|", "")
            raw = raw.replace(" ", "")
            raw = raw.replace("..", "00")     
            #      
            raw = raw.replace('\n','')
                                               
            if len(raw)!=64*32*2:
                raise Exception("Invalid frame text representation")  

            self._pixels = self._run_from_string(raw,0,64*32)               
        
    def set_pixel(self,x,y,color):
        if x==None or y==None:
            return
        if y<0 or y>31:
            return
        if x<0 or x>63:
            return
        self._pixels[y*64+x] = color
        
    def get_pixel(self,x,y):
        if x==None or y==None:
            return
        if y<0 or y>31:
            return None
        if x<0 or x>63:
            return None
        return self._pixels[y*64+x]        
    
    def draw_sprite(self,x,y, sprite):
        for yy in range(0,len(sprite)):
            for xx in range(0,len(sprite[yy])):
                self.set_pixel(x+xx,y+yy,sprite[yy][xx])
                
    def _data_run(self, data,pos,count):
        ret = ''
        for x in range(pos,pos+count):
            v = hex(data[x])[2:].upper()
            if len(v)==1:
                v = "0"+v
            if v=='00':
                v = '..'
            ret = ret + v + " "
        return ret
            
    def to_string(self):
        ret = "%\n----------------------------------------------------------\n"       
        for y in range(0,32):            
            v = self._data_run(self._pixels,y*64,64)
            v = v[0:96]+"| "+v[96:]
            if y==16:
                ret = ret + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"            
            ret = ret + v + "\n"        
        ret = ret + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
        ret = ret + "\n"
        
        return ret
    
    def _run_from_string(self,s,binOffset,count):
        ret = [0] * count
        binOffset = binOffset * 2
        for x in range(0,count):
            ret[x] = int(s[binOffset+x*2:binOffset+x*2+2],16)      
        return ret    
    
    def get_binary(self):
        # No translations needed
        return self._pixels


frame = SignFrame()
for i in range(32):
    frame.set_pixel(i,i,i)

b = frame.get_binary()

frame2 = SignFrame(frame.to_string())

print(frame2.to_string())         