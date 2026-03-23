from textual.app import App
from textual.widget import Widget
from textual.widgets import Button, Header, Input, Label

class LabelledInput(Widget):
    """LabelledInput je nas custom Widget slozeny z nekolika jinych widgetu.
    V terminologii Textual je to Compound Widget, taky si to muzeme predstavit jako group.
    """
    DEFAULT_CSS = """
    LabelledInput {
        height: 4;
    }
    """
    def __init__(self, label):
        """Potrebujeme, aby nas widget prijimimal atribut label pri sve iniciaci.
        Takze overridujeme funkci __init__() a pridavame do ni parametr label.
        Ale to prinasi problem - tim prepiseme puvodni medotu Widget.__init__(),
        ktera na pozadi dela spoustu magie. Toto je casty problem pri dedeni z tridy
        a prepisovani __init__(). Reseni je ziskat rodicovskou tridu pres super()
        a na ni pak volat .__init__(). Nacez pokracujeme custom codem...
        """
        super().__init__() # funkce super() vraci rodice tj. tridu Widget. Na ni volame puvodni konstruktor __init__()
        self.label = label # a tady pokracujeme vlastnim kodem

    def compose(self):
        yield Label(f"{self.label}:")
        yield Input(placeholder=self.label.lower())


class MyApp(App):
    def compose(self):
        yield Header(show_clock=True, icon="👻")
        yield LabelledInput("Name")
        yield LabelledInput("Surname")
        yield LabelledInput("Email")
        yield Button("Click me!")

MyApp().run()
