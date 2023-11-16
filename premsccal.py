import tkinter as tk
import math

class PremiumScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Premium Scientific Calculator")
        self.geometry("400x600")
        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for display
        entry = tk.Entry(self, textvar=self.result_var, width=16, font=('Arial', 20), borderwidth=5, justify='right')
        entry.grid(row=0, column=0, columnspan=5)

        # Define buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^2', 5, 3),
            ('sqrt', 6, 0), ('(', 6, 1), (')', 6, 2), ('C', 6, 3)
        ]

        # Add buttons to the grid
        for button_text, row_val, col_val in buttons:
            button = tk.Button(self, text=button_text, padx=20, pady=20, font=('Arial', 12),
                               command=lambda button_text=button_text: self.on_click(button_text))
            button.grid(row=row_val, column=col_val)

    def on_click(self, button_value):
        current = self.result_var.get()

        if button_value == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_value == 'C':
            self.result_var.set("")
        elif button_value == 'sqrt':
            try:
                result = math.sqrt(float(current))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_value == '^2':
            try:
                result = math.pow(float(current), 2)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(str(current) + str(button_value))

if __name__ == "__main__":
    app = PremiumScientificCalculator()
    app.mainloop()
