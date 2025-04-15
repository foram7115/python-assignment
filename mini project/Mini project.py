import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = tk.Entry(root, textvariable=self.input_text, font=('Arial', 20), bd=10, insertwidth=2, width=24, borderwidth=4, relief='ridge', justify='right')
        self.input_frame.grid(row=0, column=0, columnspan=5)

        self.create_buttons()

    def click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        elif value == "C":
            self.expression = ""
            self.input_text.set("")
        elif value in ("sin", "cos", "tan", "log", "sqrt", "exp"):
            try:
                val = eval(self.expression)
                func = getattr(math, value)
                result = str(func(val))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(value)
            self.input_text.set(self.expression)

    def create_buttons(self):
        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'log'],
            ['1', '2', '3', '-', 'exp'],
            ['0', '.', '=', '+', 'C'],
            ['sin', 'cos', 'tan', '(', ')']
        ]

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                tk.Button(self.root, text=btn, padx=20, pady=20, font=('Arial', 14),
                          command=lambda b=btn: self.click(b)).grid(row=i+1, column=j)

def main():
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
