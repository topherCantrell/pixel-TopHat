
class HatFrame:
    
    def __init__(self,s):
        self.topEdges = [0] * (27+27)
        self.topRing =  [0] * 241
        self.sideBrim = [0] * (256*6)
        
        lines = s.split("\\r?\\n");
        raw = "";
                
        '''
        for(String r : lines) {
            raw = raw + r;
        }
        raw = raw.replaceAll("-", "");
        raw = raw.replaceAll("\\|", "");
        raw = raw.replaceAll(" ", "");
        raw = raw.replaceAll("\\.\\.", "00");        
        
        if(raw.length()!=1831*2) {
            throw new RuntimeException("Invalid frame text representation");
        }
        
        topEdges = runFromString(raw,0,54);
        topRing = runFromString(raw,54,241);
        sideBrim = runFromString(raw,295,256*6);
        '''        
        
    def set_side_brim_pixel(self,x,y,color):
        if y<0 or y>23:
            return
        while x<0:
            x += 64
        while x>63:
            x -= 64
        self.sideBrim[y*64+x] = color
        
    def get_side_brim_pixel(self,x,y):
        if y<0 or y>23:
            return
        while x<0:
            x += 64
        while x>63:
            x -= 64
        return self.sideBrim[y*64+x]
    
    def set_pixel(self,p,color):
        if p<54:
            self.topEdges[p] = color
        elif p<295:
            self.topRing[p-54] = color
        else:
            self.sideBrim[p-295] = color
    
    def set_pixel(self,p):
        if p<54:
            return self.topEdges[p]
        elif p<295:
            return self.topRing[p-54]
        else:
            return self.sideBrim[p-295]
        
    def set_line(self,n,color):
        raise Exception("Implement me")
    
    def set_ring(self,n,color):
        raise Exception("Implement me")
    
    def draw_sprite(self,x,y, sprite):
        for yy in xrange(0,len(sprite)):
            for xx in xrange(0,len(sprite[yy])):
                self.set_side_brim_pixel(x+xx,y+yy,sprite[yy][xx])
                
    def _data_run(self, data,pos,count):
        ret = ''
        for x in xrange(pos,pos+count):
            v = int(data[x],16).toupper()
            if len(v)==1:
                v = "0"+v
            if v=='00':
                v = '..'
            ret = ret + v + " "
            
    def to_string(self):
        ret = "----------------------------------------------------------\n"
        ret = ret + self._data_run(self.topEdges,0,27)
        ret = ret + "; 27\n"
        ret = ret + self._data_Run(self.topEdges,27,27);
        ret = ret + "; 27\n"
        ret = ret + "----------------------------------------------------------\n"
        # Ring
        i = 0
        ret = ret + self._data_run(self.topRing,i,1)+"; 1\n"
        i = i + 1
        ret = ret + self._data_run(self.topRing,i,8)+"; 8\n"
        i = i + 8
        ret = ret + self._data_run(self.topRing,i,12)+"; 12\n"
        i = i + 12
        ret = ret + self._data_run(self.topRing,i,16)+"; 16\n"
        i = i + 16
        ret = ret + self._data_run(self.topRing,i,24)+"; 24\n"
        i = i + 24
        ret = ret + self._data_run(self.topRing,i,32)+"; 32\n"
        i = i + 32
        ret = ret + self._data_run(self.topRing,i,40)+"; 40\n"
        i = i + 40
        ret = ret + self._data_run(self.topRing,i,48)+"; 48\n"
        i = i + 48
        ret = ret + self._data_run(self.topRing,i,60)+"; 60\n"
        i = i + 60
        ret = ret + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
        # SideBrim
        for y in xrange(0,24):            
            v = self._data_run(sideBrim,y*64,64)
            v = v[0:96]+"| "+v[96:]
            if y==8 or y==16:
                ret = ret + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"            
            ret = ret + v + "\n"        
        ret = ret + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
        
        return ret
    
    def _run_from_string(self,s,binOffset,count):
        ret = [0] * count
        binOffset = binOffset * 2
        for x in xrange(0,count):
            ret[x] = int(s[binOffset+x*2:binOffset+x*2+2],16)      
        return ret
    
    