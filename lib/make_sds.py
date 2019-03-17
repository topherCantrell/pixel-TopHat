import pixel_hat

color_cursor = 0

def readLines(filename):
    with open(filename,"r") as f:
        lines = f.read().split("\n")
        ret = []
        for line in lines:
            if ';' in line:
                i = line.index(';')
                line = line[0:i]
            line = line.strip()
            if len(line)>0:
                ret.append(line)    
        return ret

def parse_color_spec(spec):
    global color_cursor
    spec = spec.replace('_','').strip()
    if '@' in spec:
        i = spec.index('@')
        crs = spec[i+1:].strip()
        spec = spec[0:i].strip()
        color_cursor = int(crs,16)
    if color_cursor>255:
        raise Exception('Exceeded 256 colors')
    g = color_cursor
    color_cursor += 1
    
    if spec.startswith('rgb'):
        i = spec.index('(')
        j = spec.rindex(')')
        frags = spec[i+1:j].split(',')
        spec = '00'+frags[1].strip()+frags[0].strip()+frags[2].strip()
    
    return g,int(spec,16)    
    
def readMovie(filename):    
    global color_cursor
    color_cursor = 0
    ret = {
        "colors" : [0]*256, 
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
            cps,col = parse_color_spec(g[1:])
            #print(":"+hex(cps)+":"+hex(col))
            ret['colors'][cps] = col
        if g.startswith("delay "):
            ret["delay"] = int(g[6:])
            
    fs = ''
    while True:
        if pos==len(lines) or lines[pos][0]=='%':            
            ret["frames"].append(pixel_hat.HatFrame(fs))            
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
    
    #ROOT = "../CHRISTMAS2018"
    #ROOT = "../FRC2018"
    #ROOT = "../FLL2018"
    ROOT = "../FRC2019"
        
    master = readLines("%s/master.txt" % (ROOT,))
    
    movies = []
    for m in master:
        # TODO labels and GOTO
        if m[0]!=':':
            movies.append(readMovie("%s/%s" % (ROOT,m)))
        
    binA = open("%s/a.bin" % (ROOT,),"wb")
    binB = open("%s/b.bin" % (ROOT,),"wb")
    
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
        # 0123 - frame count (0 to repeat disk)
        # 4567 - delay
        #89AB - Next movie sector (0 to fall into next movie)
    
        print(m["name"])
        # Write 1 sector info NUMFRAMES,DELAY
        dt = fourByteNumber(len(m["frames"]))
        binA.write(dt)
        binB.write(dt)
        dt = fourByteNumber(m["delay"])
        binA.write(dt)
        binB.write(dt)    
        dt = fourByteNumber(0) # TODO Sector number or 0 for next
        binA.write(dt)
        binB.write(dt)        
        for x in range(0,512-12):
            binA.write(b'\x00')
            binB.write(b'\x00')
        
        # Write 2 sectors colors
        for x in range(0,256):
            if x<len(m["colors"]):
                dt = fourByteNumber(m["colors"][x])
            else:
                dt = fourByteNumber(0)
            binA.write(dt)
            binB.write(dt)
            
        for f in m["frames"]:
            d = f.get_binary(True)
            if len(d)!=1024:
                raise Exception("Size")
            binA.write(d)
            d = f.get_binary(False)
            if len(d)!=1024:
                raise Exception("Size "+str(len(d)))
            binB.write(d)
            
    # Write a blank sector on the end of the file. This makes a frame count of
    # zero, which restarts the disk
    
    binA.write(bytes([0]*512))
    binB.write(bytes([0]*512))
    
    binA.flush()
    binA.close()
    binB.flush()
    binB.close()
