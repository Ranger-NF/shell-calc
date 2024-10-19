from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Static

class CalculatorDisplay(Static):
    def on_mount(self) -> None:
        self.update("Hi")

class CalculatorInterface(Static):
    def compose(self) -> ComposeResult:

        for num_on_button in range(0, 10):
            yield Button(str(num_on_button), id=f"number-{str(num_on_button)}")

class Calculator(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield CalculatorInterface()


if __name__ == "__main__":
    app = Calculator()
    app.run()
