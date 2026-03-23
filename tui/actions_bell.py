from textual.app import App
from textual.widgets import Footer, Label

class MyApp(App):
  BINDINGS = [
    ("b", "bell", "Ring"),
    ("q", "quit", "Get me out of here!!!")
    ]
  # "b" je tlacitko triggeruji action
  # "bell" je nazev action, automaticky vola funkci action_bell - action_ je apendovano implicitne!
  # "Ring" je nazev akce zobrazeny ve Footeru, bez nazvu by akce nebyla zobrazena ve footeru

  def compose(self):
    yield Footer()

  def action_bell(self):
    """Automaticky volano pri akci ring. Pozor predpona action_ je pridana automaticky, implicitne."""
    self.bell()
    self.mount(Label("Ring!"))

  def action_quit(self):
    """Akce quit automaticky implicitne pocita s tim, ze bude volat funkci s nazvem 'action_'+'quit'
    neboli prave action_quit. """
    exit()

MyApp().run()
