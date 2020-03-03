import tornado.web
import tornado.ioloop
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        x = random.randint(0,30)
        self.write("HI! Your lucky number for today is: " + str(x) + "!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
