from textual.app import App, ComposeResult
from textual.screen import ModalScreen, Screen
from textual.widgets import Footer, Placeholder, Button, Label
from textual.containers import Grid


class DashboardScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Dashboard Screen")
        yield Footer()


class SettingsScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Settings Screen")
        yield Footer()


class HelpScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Help Screen")
        yield Footer()

class QuitScreen(ModalScreen[bool]):  
    """Screen with a dialog to quit."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),        
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"), 
            id="dialog",
            )
 
    def on_button_pressed(self, event) -> None:
            if event.button.id == "quit":
                self.dismiss(True)
            else:
                self.dismiss(False)


class ModesApp(App):
    BINDINGS = [
        ("d", "switch_mode('dashboard')", "Dashboard"),  
        ("s", "switch_mode('settings')", "Settings"),
        ("h", "switch_mode('help')", "Help"),
        ("q", "quit()", "Quit"),
        ("a", "ask()", "Ask"),
    ]
    MODES = {
        "dashboard": DashboardScreen,  
        "settings": SettingsScreen,
        "help": HelpScreen,
    }
    def on_quit(self) -> None:
        self.exit()

    def on_mount(self) -> None:
        self.switch_mode("dashboard")

    def action_ask(self) -> None:
        def check_quit(quit: bool | None) -> None:
            """Called when QuitScreen is dismissed."""
            if quit:
                self.exit()

        self.push_screen(QuitScreen(), check_quit)


if __name__ == "__main__":
    app = ModesApp()
    app.run()