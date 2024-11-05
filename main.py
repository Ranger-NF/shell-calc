from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Static

current_display_chars = ""
supported_operation = ["+", "-", "*", "/"]

class CalculatorDisplay(Static):
    def on_mount(self) -> None:
        self.update(current_display_chars)

class CalculatorInterface(Static):
    def compose(self) -> ComposeResult:

        yield CalculatorDisplay()
        for num_on_button in range(0, 10):
            yield Button(str(num_on_button), id=f"number-{str(num_on_button)}")

    def process_input(self, input_value: str):
        if not input_value in supported_operation:
            current_display_chars += input_value

    def on_button_pressed(self, event: Button.Pressed):
        display = self.query_one(CalculatorDisplay)

        if event.button.id != None:
            button_num = event.button.id.split("-")[1]

            display.update(button_num)
        # match event.button.id:
        #     case

class Calculator(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield CalculatorInterface()


if __name__ == "__main__":
    app = Calculator()
    app.run()
