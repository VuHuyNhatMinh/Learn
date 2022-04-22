# Import everything from tkinter module
from tkinter import *

# Following will import tkinter.ttk module and automatically override all the widgets
# which are present in tkinter module
from tkinter.ttk import *

# Create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry("100x100")

# Create a Butoon
btn = Button(root, text = "Click me!", command = root.destroy)

# Set the position of button on the top of window.
btn.pack(side = "top")
root.mainloop()