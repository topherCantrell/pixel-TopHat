
class SpriteLoader:
    
    def __init__(self):
        
        self.sprites = {}
        
        with open("..\Sprites.txt") as f:
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
        ret = [[[] for i in range(len(sprite[0]))] for i in range(len(sprite))]        
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
    
    def flipLeftRight(self,colorSprite):
        pass
    
    def flipUpDown(self,colorSprite):
        pass
    

if __name__ == '__main__':
    
    sp = SpriteLoader()