import tornado.ioloop
import tornado.web
import tornado.websocket

#example hello world pro websocket komunikaci

class MainHandler(tornado.web.RequestHandler):
    """
    MainHandler obstarava index page na adrese "/"
    """
    def get(self):
        self.render("index.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler): # pozor neimportujeme bezny tornado.web.RequestHandler
    """
    WebSocketHandler obstarava Websocket komunikaci na adrese /websocket
    """
    def open(self): #vola se pri otevreni komunikace / pripojeni prohlizece
        print("WebSocket opened")

    def on_message(self, message): #pri prichodu nove zpravy
        self.write_message(u"You said: " + message) # odesilame zpravu pres websocket

    def on_close(self): #pri uzavreni komunikace / odpojeni prohlizece
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocketHandler),
        (r"/src/(.*)", tornado.web.StaticFileHandler, {"path": "src/"}),
        # pouzivame primo bez uprav tornado.web.StaticFileHandler
        # ten slouzi k zobrazovani statickych souboru (.js, .css, .jpeg atd...)
        # zde ho mame kvuli souboru websocket.js - jinak by se nedal nacist
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
