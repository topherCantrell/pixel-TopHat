import HatFrame

def readLines(filename):
    f = open(filename,"r")
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
    ret = {"colors" : [], "delay" : 0, "frames" : [], "name" : ''}
    
    i = filename.index(".")
    ret["name"] = filename[0:i]
    
    if len(ret["name"])>15:
        raise Exception("Name must be less than 16 characters: "+ret["name"])
    lines = readLines("../"+filename)
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
            ret["delay"] = int(g[6])
            
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
            
        

    
    
master = readLines("../master.txt")

movies = []
for m in master:
    movies.append(readMovie(m))
    
