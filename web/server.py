import tornado.ioloop
import tornado.web
import os
import serial
        
class CGIHandler(tornado.web.RequestHandler):
    def get(self,first):        
        self.write(":"+first+":")
        ser.write(bytes(first+"\n"))

#ser = serial.Serial('COM9',115200)
ser = serial.Serial('/dev/serial0',115200)

root = os.path.join(os.path.dirname(__file__), "webroot")

handlers = [
    (r"/cgi/(.*)", CGIHandler),        
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
    ]

app = tornado.web.Application(handlers)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()