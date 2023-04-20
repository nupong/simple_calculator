from tkinter import *

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display widget
        self.display = Entry(master, width=25, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Create buttons
        button = Button(master, text="Clear", width=5, height=2, command=lambda val='C': self.click(val))
        button.grid(row=1, column=3, padx=1, pady=1)
        button_values = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        r = 2
        c = 0
        for value in button_values:
            button = Button(master, text=value, width=5, height=2, command=lambda val=value: self.click(val))
            button.grid(row=r, column=c, padx=1, pady=1)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def click(self, value):
        if value == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, END)
                self.display.insert(END, result)
            except:
                self.display.delete(0, END)
                self.display.insert(END, "Error")
        elif value == 'C': # added code to clear the display here
            self.display.delete(0, END)
        else:
            self.display.insert(END, value)

root = Tk()
calculator = Calculator(root)
root.mainloop()
