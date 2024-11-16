from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Static

current_display_chars: str = "0"
supported_operations = ("+", "-", "*", "/")

names_of_symbols = {
    "+": "add",
    "-": "substract",
    "*": "multiply",
    "/": "divide"
}

class CalculatorDisplay(Static):
    def on_mount(self) -> None:
        self.update(current_display_chars)

class CalculatorInterface(Static):
    previous_terms: list[int] = []

    def compose(self) -> ComposeResult:

        yield CalculatorDisplay()
        for num_on_button in range(0, 10):
            yield Button(str(num_on_button), id=f"number-{str(num_on_button)}")

        for symbol in supported_operations: # TO BE WORKED ON
            yield Button(symbol, id=f"operator-{names_of_symbols[symbol]}")

    def add_to_term(self, input_value: str):
        global current_display_chars

        display = self.query_one(CalculatorDisplay)

        if current_display_chars == "0":
            current_display_chars = input_value
        else:
            current_display_chars += input_value

        display.update(current_display_chars)

    def add_operation(self, operation_type):
        pass

    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id != None:
            button_info = event.button.id.split("-")
            button_type = button_info[0]
            button_char = button_info[1]

            if button_type == "number":
                self.add_to_term(button_char)
            elif button_type == "symbol":


class Calculator(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield CalculatorInterface()


if __name__ == "__main__":
    app = Calculator()
    app.run()
