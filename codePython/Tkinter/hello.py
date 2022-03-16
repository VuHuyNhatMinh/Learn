from tkinter import *

# root window
root = Tk()

# Creating a Label Widget
myLabel = Label(root, text = "Hello World!")

# put into the root window
# 1. pack: as big as the widget inside it.
myLabel.pack()

# Looping
# x --> close the main loop
root.mainloop()