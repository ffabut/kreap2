import tornado.ioloop
import tornado.web

#ukazka toho, jak na jedne adrese (a tedy v jednom handleru)
#zobrazovat jak stranku pro zadani dat (skrze metodu GET)
#tak prijimat data (skrz metodu POST)

class MainHandler(tornado.web.RequestHandler):
    """
    MainHandler obstarava index page na adrese "/" (kdy dostane GET request)
    a zaroven prijima data na stejne adrese pri POST requestu
    """
    def get(self):
        #pri GET requestu zobrazime stranku s formularem
        self.render("index.html")

    def post(self):
        #uzivatelka zadala data a ta se poslala jako POST request na stejnou adresu, tedy "/"
        # u POST requestu zpracujeme prichozi data

        # jmeno argumentu se musi shodovat s tim, jak je pojmenovane pole ve formulari <form>
        jmeno = self.get_argument("name") #pokud nezadame pojmenovany parametr "default", pak dojde k chybe pri nedodani dat
        email = self.get_argument("mail", default="email") #pokud zadame default, pak pri nedodani dat se pouzije hodnota v default
        
        self.write(jmeno + " " + email) #nakonec vratime stranku s jednoduchym echem vlozenych dat
        #pripadne taky muze byt render() nebo redirect()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), #hlavni handler pro index page
        #nepotrebujeme zadny dalsi handler, je to 2v1!
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()