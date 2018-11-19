
class SpriteLoader:
    
    def __init__(self):
        
        self.sprites = {}
        
        with open("Sprites.txt") as f:
            lines = f.readlines()
            
        currentName = None
        currentSprite = []
        
        for line in lines:
            line = line.strip()
            if len(line)==0:
                continue
            if line[0]=='-':
                if currentName != None:
                    self.sprites[currentName] = currentSprite
                currentName = line[1:]
                currentSprite = []
                continue
            currentSprite.append(line)            
            
        if currentName != None:
            self.sprites[currentName] = currentSprite            
            
    def colorSprite(self,name,colorMap):
        sprite = self.sprites[name]
        ret = [[[] for _ in range(len(sprite[0]))] for _ in range(len(sprite))]        
        for y in range(0,len(sprite)):
            s = sprite[y]
            for x in range(len(s)):
                c = s[x]
                v = 0
                if c=='.' or c==' ':
                    v = 0
                else:
                    for z in range(0,len(colorMap),2):
                        if colorMap[z]==c:
                            v = colorMap[z+1]
                            break
                
                ret[y][x] = v
        return ret
    
    def doubler(self,colorSprite):
        ret =[]
        for y in range(0,len(colorSprite)):
            drow = []
            for x in range(0,len(colorSprite[y])):
                drow.append(colorSprite[y][x])
                drow.append(colorSprite[y][x])
            ret.append(drow)
            ret.append(drow)            
        return ret
    
    def flipLeftRight(self,sprite):
        '''
        int [][] ret = new int[colorSprite.length][colorSprite[0].length];
        for(int y=0;y<colorSprite.length;++y) {
            for(int x=0;x<colorSprite[y].length;++x) {
                ret[y][colorSprite[y].length-x-1] = colorSprite[y][x];
            }
        }
        return ret;
        '''
        ret = [[[] for _ in range(len(sprite[0]))] for _ in range(len(sprite))] 
        for y in range(0,len(sprite)):
            for x in range(0,len(sprite[y])):
                ret[y][len(sprite[y])-x-1] = sprite[y][x]            
        
        return ret
    
    def flipUpDown(self,colorSprite):
        '''
        int [][] ret = new int[colorSprite.length][];
        int i = ret.length-1;
        for(int x=0;x<colorSprite.length;++x) {
            ret[i] = colorSprite[x];
            --i;
        }        
        return ret;
        '''
    

if __name__ == '__main__':
    
    sp = SpriteLoader()