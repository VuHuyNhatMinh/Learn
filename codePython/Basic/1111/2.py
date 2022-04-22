import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

# Create the root window
root = tk.Tk()
root.title("Tkinter Message Box")
root.resizable(False, False)
root.geometry("300x150")

# 
options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text = "Show an error message",
    command = lambda: showerror(
        title = 'Error',
        message = 'This is an error message.'
    )
).pack(options)

root.mainloop()