import HatFrame

def readLines(filename):
    with open(filename,"r") as f:
        lines = f.read().split("\n")
        ret = []
        for line in lines:
            if ';' in line:
                i = line.index(';')
                line = line[0:i]
            if len(line)>0:
                ret.append(line)    
        return ret

def readMovie(filename):    
    ret = {
        "colors" : [], 
        "delay"  : 0, 
        "frames" : [], 
        "name"   : ''
    }
    
    i = filename.index(".")
    ret["name"] = filename[0:i]
    
    if len(ret["name"])>15:
        raise Exception("Name must be less than 16 characters: "+ret["name"])
    lines = readLines(filename)
    pos = 0
    while True:
        g = lines[pos]
        pos += 1
        if g[0]=='%':
            break
        if g[0]=='#':
            g = g[1:].replace('_','')
            ret["colors"].append(int(g,16))
        if g.startswith("delay "):
            ret["delay"] = int(g[6:])
            
    fs = ''
    while True:
        if pos==len(lines) or lines[pos][0]=='%':            
            ret["frames"].append(HatFrame.HatFrame(fs))            
            fs = ''
            pos+=1
        if pos>len(lines):
            break
        fs = fs + lines[pos]
        pos += 1
        
    return ret            
        
def fourByteNumber(number):    
    by = [number & 0xFF, 
          (number>>8) & 0xFF, 
          (number>>16) & 0xFF,
          (number>>24) & 0xFF
         ]
    return bytes(by)
        

if __name__=='__main__':
        
    master = readLines("master.txt")
    
    movies = []
    for m in master:
        movies.append(readMovie(m))
        
    binA = open("a.bin","wb")
    binB = open("b.bin","wb")
    
    preA = b'2018\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    binA.write(preA)
    
    preB = b'2018\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02'
    binB.write(preB)
    
    currentSector = 1
    for ent in range(0,31):   
        dt = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        if ent < len(movies):
            m = movies[ent]
            dt = b''
            for x in range(0,12):
                if x<len(m["name"]):
                    dt = dt + bytes(m["name"][x].encode('ascii'))
                else:
                    dt = dt + b'\x00'
            dt = dt + fourByteNumber(currentSector);        
            currentSector = currentSector + 3 + len(m["frames"])*2;    
        binA.write(dt)
        binB.write(dt)
        
    for m in movies:
        print(m["name"])
        # Write 1 sector info NUMFRAMES,DELAY
        dt = fourByteNumber(len(m["frames"]))
        binA.write(dt)
        binB.write(dt)
        dt = fourByteNumber(m["delay"])
        binA.write(dt);
        binB.write(dt);    
        for x in range(0,512-8):
            binA.write(b'\x00');
            binB.write(b'\x00');
        
        # Write 2 sectors colors
        for x in range(0,256):
            if x<len(m["colors"]):
                dt = fourByteNumber(m["colors"][x])
            else:
                dt = fourByteNumber(0)
            binA.write(dt);
            binB.write(dt);
            
        for f in m["frames"]:
            d = f.get_binary(True)
            if len(d)!=1024:
                raise Exception("Size")
            binA.write(d)
            d = f.get_binary(False)
            if len(d)!=1024:
                raise Exception("Size "+str(len(d)))
            binB.write(d)
    
    binA.flush()
    binA.close()
    binB.flush()
    binB.close()
