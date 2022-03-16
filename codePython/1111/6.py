import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# Create the root window
root = tk.Tk()
root.title("Tkinter File Dialog")
root.resizable(False, False)
root.geometry("300x150")
def select_files():
    filetypes = (
        ('text file', '*.txt'),
        ('All files', '*x*')
    )

    filenames = fd.askopenfilenames(
        title = "Open a file",
        initialdir = '/',
        filetypes = filetypes
    )

    showinfo(
        title = "Selected File",
        message = filenames
    )
# Open button
open_button = ttk.Button(
    root,
    text = "Open Files",
    command = select_files
)
open_button.pack(expand = True)

# Run the application
root.mainloop()