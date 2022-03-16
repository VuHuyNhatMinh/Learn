import tkinter as tk
from tkinter import ttk


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        Lb = ttk.Label(self, text='Find what:')
        Lb.grid(column=0, row=0, sticky=tk.W)

        self.keyword = ttk.Entry(self, width=30)
        self.keyword.focus()
        self.keyword.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Replace with:').grid(
            column=0, row=1, sticky=tk.W)

        self.replacement = ttk.Entry(self, width=30)
        self.replacement.grid(column=1, row=1, sticky=tk.W)

        self.match_case = tk.StringVar()
        match_case_check = ttk.Checkbutton(
            self, text='Match case', variable=self.match_case)
        match_case_check.grid(column=0, row=2, sticky=tk.W)

        self.wrap_around = tk.StringVar()
        wrap_around_check = ttk.Checkbutton(
            self, text='Wrap around', variable=self.wrap_around)
        wrap_around_check.grid(column=0, row=3, sticky=tk.W)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)


class ButtonFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        buttonList = ["Find Next", "Replace", "Replace All", "Cancel"]
        ttk.Button(self, text="Find Next", command=lambda: self.send_clicked("Find Next")).grid(
            column=0, row=0)
        ttk.Button(self, text="Replace", command=lambda: self.send_clicked("Replace")).grid(
            column=0, row=1)
        ttk.Button(self, text="Replace All", command=lambda: self.send_clicked("Replace All")).grid(
            column=0, row=2)
        ttk.Button(self, text="Cancel", command=self.quit).grid(
            column=0, row=3)
        for widgets in self.winfo_children():
            widgets.grid(padx=5, pady=3)

    def send_clicked(self, order):
        pass


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Replace")
        self.geometry('400x150')
        self.resizable(0, 0)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=1)
        self.__create_widgets()

    def __create_widgets(self):
        self.input_frame = InputFrame(self)
        self.button_frame = ButtonFrame(self)

        def change_funtion(order):
            json = {
                "order": "",
                "match_case": 0,
                "wrap_around": 0,
                "find_what": "",
                "replace_with": ""
            }
            json["order"] = order
            json["match_case"] = self.input_frame.match_case.get()
            json["wrap_around"] = self.input_frame.wrap_around.get()
            json["find_what"] = self.input_frame.keyword.get()
            json["replace_with"] = self.input_frame.replacement.get()
            print(json)
        self.button_frame.send_clicked = change_funtion
        self.input_frame.grid(column=0, row=0, sticky=tk.NSEW)
        self.button_frame.grid(column=1, row=0, sticky=tk.NSEW)


if __name__ == '__main__':
    app = App()
    app.mainloop()
