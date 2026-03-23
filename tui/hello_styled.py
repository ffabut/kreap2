from textual.app import App
from textual.widgets import Label, Static

class SimpleApp(App):
  def compose(self):
    """Compose urcuje kompozici elementu v aplikaci.
    Pod povrchem je to generator, jednotlive widgety tedy "vracime" pres yield.
    """
    self.static = Static("I am a [bold red]Static[/bold red] widget!")
    yield self.static # widgety umistime skrze yield
    self.label = Label("I am a [yellow italic]Label[/yellow italic] widget!",)
    yield self.label

  def on_mount(self):
    """on_mount je volano po tom, co jsou widgety vytvoreny a umisteny,
    ale pred tim, nez je vykresleno... Nyni je idealni aplikovat styly.
    """
    # Stylovat nemusime jen pres CSS="", ale taky pres atribut .styles widgetu
    self.static.styles.background = "blue"
    self.static.styles.border = ("solid", "white")
    self.static.styles.text_align = "center"
    self.static.styles.padding = 1, 1
    self.static.styles.margin = 4, 4
    # Styling the label
    self.label.styles.background = "darkgreen"
    self.label.styles.border = ("double", "red")
    self.label.styles.padding = 1, 1
    self.label.styles.margin = 2, 4

if __name__ == "__main__":
  app = SimpleApp()
  app.run()
