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
        ttk.Label(self, text = "Find what: ").grid(column=0, row=0, sticky=tk.W)
        self.keyword = ttk.Entry(self, width = 30)
        self.keyword.grid(column=1, row=0, sticky=tk.W)

        # Replace with
        ttk.Label(self, text = "Replace with: ").grid(column=0, row=1, sticky=tk.W)
        self.replacement = ttk.Entry(self, width = 30)
        self.replacement.grid(column=1, row=1, sticky=tk.W)

        # Match Case checkbox
        self.match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton(
            self,
            text = "Match Case",
            variable=self.match_case,
        )
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        # Wrap Around checkbox
        self.wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(
            self, 
            text = "Wrap around",
            variable=self.wrap_around,
        )
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

class ButtonFrame(InputFrame):
    def __init__(self, container):
        super().__init__(container)

        # Setup the grid layout manager
        self.columnconfigure(1, weight = 1)

        self.__create__buttons()

    def __create__buttons(self):
        # Find Next
        bt_find_next = ttk.Button(self, text="Find Next", command=lambda: self.clicked("Find Next"))
        bt_find_next.grid(column=2, row=0, sticky=tk.W)

        # Replace
        bt_replace = ttk.Button(self, text="Replace", command=lambda: self.clicked("Replace"))
        bt_replace.grid(column=2, row=1, sticky=tk.W)

        # Replace All
        bt_replace_all = ttk.Button(self, text="Replace All", command = lambda: self.clicked("Replace All"))
        bt_replace_all.grid(column=2, row=2, sticky=tk.W)

        # Cancel
        bt_cancel = ttk.Button(self, text="Cancel", command = self.quit)
        bt_cancel.grid(column=2, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
            
    def clicked(self, ck):
        json = {}

        json["order"]        = ck
        json["match_case"]   = self.match_case.get()
        json["wrap_around"]  = self.wrap_around.get()
        json["find_what"]    = self.keyword.get()
        json["replace_with"] = self.replacement.get()
        print(json)


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

        self.__create_widget()

    def __create_widget(self):
        # Create the button frame
        button_frame = ButtonFrame(self)
        button_frame.grid(column=0, row=0)

if __name__ == "__main__":
    root = App()
    root.mainloop()
