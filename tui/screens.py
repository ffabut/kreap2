from textual.app import App, ComposeResult
from textual.screen import ModalScreen, Screen
from textual.widgets import Footer, Placeholder, Button, Label, Static
from textual.containers import Grid


class WelcomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static(
r"""
________________.___.__________________                .__    _____________________________  
\__    ___/\__  |   |\______   \_____  \   ____ _____  |  |   \______   \______   \_   ___ \ 
  |    |    /   |   | |     ___//   |   \_/ ___\\__  \ |  |    |       _/|     ___/    \  \/ 
  |    |    \____   | |    |   /    |    \  \___ / __ \|  |__  |    |   \|    |   \     \____
  |____|    / ______| |____|   \_______  /\___  >____  /____/  |____|_  /|____|    \______  /
            \/                         \/     \/     \/               \/                  \/ 

Welcome to the sample text-based RPG game.

[@click=app.switch_mode('game')]Play[/@click=]
[@click=app.switch_mode('settings')]Settings[/@click=]
[@click=app.quit]Quit[/@click=]
""")


class GameScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static(
"""
You have entered a gloomy cave, it's dark like a terminal.
But fortunately you have a torch. You lit it up and start walking further and further.
After a while you see a Skeleton Mage.

What do you do?
[@click=screen.attack]Attack[/]
[@click=screen.hello]Say Hello[/]
[@click=app.quit]Run Away[/]
"""
        )
        yield Footer()

    def action_attack(self):
        """Predpona action_ je pozadovana."""
        def goto_violence(answer) -> None:
            self.app.install_screen(LevelViolenceScreen(), name="violence")
            self.app.push_screen("violence") # nevim, proc tu switch_screen failne na IndexError: pop from empty list

        def check_question(answer: bool | None) -> None:
            """Called when QuitScreen is dismissed."""
            if answer == True:
                self.app.push_screen(
                    InfoScreen(info="You killed an unarmed, non-aggressive civilian Skeleton Mage.", confirmation="Ok, boomer!"),
                    goto_violence
                )
        self.app.push_screen(
            QuestionScreen(question="Are you sure you want to attack?"),
            check_question  # setting callback function which will get return value of the QuitScreen()
            )

    def action_hello(self):
        def goto_limbo(answer) -> None:
            self.app.install_screen(LevelLimboScreen(), name="limbo")
            self.app.push_screen("limbo") # nevim, proc tu switch_screen failne na IndexError: pop from empty list
        def check_answer(answer: bool | None) -> None:
            """Called when QuitScreen is dismissed."""
            if answer == True:
                self.app.push_screen(
                    InfoScreen(info="Hey, you look like a chill, laid-back dude. Wanna grab a smoke?", confirmation="Sure thing!"),
                    goto_limbo
                )
        self.app.push_screen(
            QuestionScreen(question="Do you think this is a good idea?"),
            check_answer  # setting callback function which will get return value of the QuitScreen()
            )

class LevelLimboScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static(
"""
Here, as mine ear could note, no plaint was heard
except of sighs, that made the eternal air
tremble, not caused by tortures, but from grief
felt by those multitudes, many and vast,
of men, women, and infants. 
"""
    )
        yield Footer()


class LevelViolenceScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static(
"""
We with our faithful escort onward moved
  Along the brink of the vermilion boiling,
  Wherein the boiled were uttering loud laments.

People I saw within up to the eyebrows,
  And the great Centaur said: "Tyrants are these,
  Who dealt in bloodshed and in pillaging.
"""
    )
        yield Footer()


class SettingsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Settings Screen")
        yield Footer()


class QuestionScreen(ModalScreen[bool]):
    """Popup window pro zeptani se hracstva na otazku ANO/NE."""
    def __init__(self, question="Are you sure?"):
        super().__init__()
        self.question = question

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.question, id="question"),        
            Button("Yes", variant="error", id="yes"),
            Button("No", variant="primary", id="no"), 
            id="question_dialog",
            )
 
    def on_button_pressed(self, event) -> None:
        if event.button.id == "yes":
            self.dismiss(True) # funguje jako return - zavre okno a vrati True
        else:
            self.dismiss(False) # return


class InfoScreen(ModalScreen[bool]):
    """Popup window pro informovani hracstva, muze byt jen potvrzeno."""
    def __init__(self, info="Are you sure?", confirmation="ok"):
        super().__init__()
        self.info = info
        self.confirmation = confirmation

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.info, id="info"),        
            Button(self.confirmation, variant="primary", id="confirmation"), 
            id="info_dialog",
            )
 
    def on_button_pressed(self, event) -> None:
        self.dismiss(True) # funguje jako return - zavre okno a vrati True
        

class ModesApp(App):
    CSS_PATH = "screens.tcss"
    BINDINGS = [
        ("g", "switch_mode('game')", "Game"),  
        ("s", "switch_mode('settings')", "Settings"),
        ("w", "switch_mode('welcome')", "Welcome"),
        ("q", "quit()", "Quit"),
    ]
    # Modes jsou nezavisle stacky screens, muzeme tak vrstvit screens a kdyz prepneme
    # do dalsiho mode, pouzije se nezavisla sada navrstvenych screens
    MODES = {
        "welcome": WelcomeScreen,
        "game": GameScreen,
        "settings": SettingsScreen,
    }
    def on_quit(self) -> None:
        self.exit()

    def on_mount(self) -> None:
        self.switch_mode("welcome")


if __name__ == "__main__":
    app = ModesApp()
    app.run()
