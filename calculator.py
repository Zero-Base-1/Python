import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        # Variables to store calculation data
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.result = False
        self.operator = ""
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.window)
        display_frame.pack(expand=False, fill="both")
        
        display = tk.Entry(display_frame, textvariable=self.display_var, 
                          font=("Arial", 16), bd=10, insertwidth=4,
                          width=14, justify="right", state="readonly")
        display.pack(side="top")
        
        # Button frame
        button_frame = tk.Frame(self.window)
        button_frame.pack(expand=True, fill="both")
        
        # Row 0: Clear and Backspace
        tk.Button(button_frame, text="C", width=10, height=3, 
                 command=self.clear_all).grid(row=0, column=0, columnspan=2, sticky="nsew")
        tk.Button(button_frame, text="⌫", width=5, height=3, 
                 command=self.backspace).grid(row=0, column=2, columnspan=2, sticky="nsew")
        
        # Row 1: 7, 8, 9, /
        tk.Button(button_frame, text="7", width=5, height=3, 
                 command=lambda: self.number_press(7)).grid(row=1, column=0, sticky="nsew")
        tk.Button(button_frame, text="8", width=5, height=3, 
                 command=lambda: self.number_press(8)).grid(row=1, column=1, sticky="nsew")
        tk.Button(button_frame, text="9", width=5, height=3, 
                 command=lambda: self.number_press(9)).grid(row=1, column=2, sticky="nsew")
        tk.Button(button_frame, text="÷", width=5, height=3, 
                 command=lambda: self.operation_press("/")).grid(row=1, column=3, sticky="nsew")
        
        # Row 2: 4, 5, 6, *
        tk.Button(button_frame, text="4", width=5, height=3, 
                 command=lambda: self.number_press(4)).grid(row=2, column=0, sticky="nsew")
        tk.Button(button_frame, text="5", width=5, height=3, 
                 command=lambda: self.number_press(5)).grid(row=2, column=1, sticky="nsew")
        tk.Button(button_frame, text="6", width=5, height=3, 
                 command=lambda: self.number_press(6)).grid(row=2, column=2, sticky="nsew")
        tk.Button(button_frame, text="×", width=5, height=3, 
                 command=lambda: self.operation_press("*")).grid(row=2, column=3, sticky="nsew")
        
        # Row 3: 1, 2, 3, -
        tk.Button(button_frame, text="1", width=5, height=3, 
                 command=lambda: self.number_press(1)).grid(row=3, column=0, sticky="nsew")
        tk.Button(button_frame, text="2", width=5, height=3, 
                 command=lambda: self.number_press(2)).grid(row=3, column=1, sticky="nsew")
        tk.Button(button_frame, text="3", width=5, height=3, 
                 command=lambda: self.number_press(3)).grid(row=3, column=2, sticky="nsew")
        tk.Button(button_frame, text="−", width=5, height=3, 
                 command=lambda: self.operation_press("-")).grid(row=3, column=3, sticky="nsew")
        
        # Row 4: 0, ., =, +
        tk.Button(button_frame, text="0", width=5, height=3, 
                 command=lambda: self.number_press(0)).grid(row=4, column=0, sticky="nsew")
        tk.Button(button_frame, text=".", width=5, height=3, 
                 command=self.decimal_press).grid(row=4, column=1, sticky="nsew")
        tk.Button(button_frame, text="=", width=5, height=3, 
                 command=self.equals_press).grid(row=4, column=2, sticky="nsew")
        tk.Button(button_frame, text="+", width=5, height=3, 
                 command=lambda: self.operation_press("+")).grid(row=4, column=3, sticky="nsew")
        
        # Configure grid weights for responsive design
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def number_press(self, num):
        if self.input_value:
            if self.current == "0":
                self.current = str(num)
            else:
                self.current = self.current + str(num)
        else:
            self.current = str(num)
            self.input_value = True
        
        self.display_var.set(self.current)
    
    def decimal_press(self):
        if self.input_value:
            if "." not in self.current:
                self.current = self.current + "."
        else:
            self.current = "0."
            self.input_value = True
        
        self.display_var.set(self.current)
    
    def operation_press(self, op):
        if not self.result:
            self.calculate()
        
        self.operator = op
        if self.current:
            self.total = float(self.current)
        self.input_value = False
        self.result = False
    
    def equals_press(self):
        if self.operator and self.input_value:
            self.calculate()
            self.operator = ""
            self.input_value = False
            self.result = True
    
    def calculate(self):
        try:
            if self.operator == "+":
                self.total += float(self.current)
            elif self.operator == "-":
                self.total -= float(self.current)
            elif self.operator == "*":
                self.total *= float(self.current)
            elif self.operator == "/":
                if float(self.current) == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    self.clear_all()
                    return
                self.total /= float(self.current)
            
            # Format the result to remove unnecessary decimal places
            if self.total == int(self.total):
                self.current = str(int(self.total))
            else:
                self.current = str(round(self.total, 10))
            
            self.display_var.set(self.current)
            
        except Exception as e:
            messagebox.showerror("Error", "Invalid operation!")
            self.clear_all()
    
    def clear_all(self):
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.result = False
        self.operator = ""
        self.display_var.set("0")
    
    def backspace(self):
        if self.input_value and len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
            self.input_value = True
        
        self.display_var.set(self.current)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
