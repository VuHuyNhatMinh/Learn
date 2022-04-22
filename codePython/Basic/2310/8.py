# Import tkinter module, app6.py
from tkinter import *

# Creating Tk window
master = Tk()

# Setting geometry of tk window
master.geometry("200x200")

# Button widget
b1 = Button(master, text = "Click me!")
b1. place(relx = 1, x = -2, y = 2, anchor = NE)

# Label widget
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# Button widget
b2 = Button(master, text = "GFG")
b2.place(relx = 0.5, rely  = 0.5, anchor = CENTER)

master.mainloop()
