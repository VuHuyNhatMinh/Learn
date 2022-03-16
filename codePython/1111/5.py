import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Create the root window
root = tk.Tk()
root.title("Tkinter Open File Dialog")
root.resizable(False, False)
root.geometry("300x150")

def select_file():
    filetypes = (
        ('text file', '*.txt'),
        ('All files', '*x*')
    )

    filename = fd.askopenfilename(
        title = "Open a file",
        initialdir = '/',
        filetypes = filetypes
    )

    showinfo(
        title = "Selected File",
        message = filename
    )

# Open button
open_button = ttk.Button(
    root,
    text = "Open a File",
    command = select_file
)

open_button.pack(expand = True)

# Run the application
root.mainloop()