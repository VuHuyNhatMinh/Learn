import tkinter as tk
from tkinter import ttk

class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Setup the grid layout manager
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 3)

        self.__create_widgets()
    
    def __create_widgets(self):
        # Find what
        Lb = ttk.Label(self, text = "Find what: ")
        Lb.grid(column=0, row=0, sticky=tk.W)

        keyword = ttk.Entry(self, width = 30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with
        ttk.Label(self, text = "Replace with: ").grid(column=0, row=1, sticky=tk.W)
        replacement = ttk.Entry(self, width = 30)
        replacement.grid(column=1, row=1, sticky=tk.W)

        # Match Case checkbox
        match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton(
            self,
            text = "Match Case",
            variable=match_case,
            command=lambda: print(match_case.get()),
        )
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        # Wrap Around checkbox
        wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(
            self, 
            variable=wrap_around,
            text = "Wrap around",
            command=lambda: print(wrap_around.get()),
        )
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # Setup the grid layout manager
        self.columnconfigure(1, weight = 1)
        # self.columnconfigure(1, weight = 3)
 
        self.__create__buttons()

    def __create__buttons(self):
        # Find Next
        bt_find_next = ttk.Button(self, text="Find Next")
        bt_find_next.grid(column=1, row=0, sticky=tk.W)

        # Replace
        bt_replace = ttk.Button(self, text="Replace")
        bt_replace.grid(column=1, row=1, sticky=tk.W)

        # Find Next
        bt_replace_all = ttk.Button(self, text="Replace All")
        bt_replace_all.grid(column=1, row=2, sticky=tk.W)

        # Find Next
        bt_cancel = ttk.Button(self, text="Cancel")
        bt_cancel.grid(column=1, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Replace")
        self.geometry("400x150")
        self.resizable(0, 0)
        # Window only (remove the minimize/maximize button)
        self.attributes("-toolwindow", True)
        
        # Layout on the root window
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        
        self.__create_widgets()


    def __create_widgets(self):
        # Create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

        # Create the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(column=1, row=0)

if __name__ == "__main__":
    root = App()
    root.mainloop()
