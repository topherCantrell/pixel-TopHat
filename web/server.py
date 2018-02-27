import tornado.ioloop
import tornado.web
import os
        
class CGIHandler(tornado.web.RequestHandler):
    def get(self,first):
        if (first=="chris"):
            self.write("Hi Chris ")
        self.write(":"+first+":")
        print "PYSERIAL:"+first+":"
        # send "first" and line-feed over pyserial

root = os.path.join(os.path.dirname(__file__), "webroot")

handlers = [
    (r"/cgi/(.*)", CGIHandler),        
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
    ]

app = tornado.web.Application(handlers)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()