import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Tkinter MVC Demo")
        self.geometry("300x100")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.__create_widgets()
    
    def __create_widgets(self):
        
        self.frame = ttk.Frame(self)
        self.frame.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.W)

        for index in [0, 1, 2]:
            self.frame.columnconfigure(index, weight = 1)
        self.frame.rowconfigure(0, weight = 1)

        self.label = ttk.Label(self.frame, text = "Email:")
        self.label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.W)

        self.entry = ttk.Entry(self.frame, width = 30)
        self.entry.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.W)

        self.button = ttk.Button(self.frame, text = 'Save')
        self.button.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = tk.W)

if __name__ == '__main__':
    app = App()
    app.mainloop()