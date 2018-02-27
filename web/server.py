import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind( ("", 8888))
s.listen(1)

while True:
    
    conn, addr = s.accept()
    
    try:    
        g = ""
        
        while "\n" not in g:
            chunk = conn.recv(80)
            if not chunk:
                break
            g = g + chunk
            
        url = g.split(" ")[1]
        
        # /                The index.html
        # /cgi/command     A display command
        # <anything else>  A static file
        
        print url
        
        if url=="/":
            print "ROOT"
            pass
        elif url.startswith("/cgi/"):     
            print "CGI:"+url       
            pass
        else:
            # Attempt to send back static file
            print "LOAD FILE"   
            pass     
        
    except:
        # Doesn't matter what happened. Ignore it.
        pass
    
    finally:
        # Always try to close the connection
        try:
            conn.close()
        except:
            pass
    
    