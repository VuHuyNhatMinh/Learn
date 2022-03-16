from tkinter import *
''' 2 step: creating and shoving on the screen'''
# root window
root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My name is Ethan.")
# Python is oop language.
# myLabel1 = Label(root, text = "Hello World!").grid(row=0, column=0)
# myLabel2 = Label(root, text = "My name is Ethan.").grid(row=1, column=0)

# put into the root window
# Position is relative.
myLabel1.grid(row = 0, column=0)
myLabel2.grid(row = 1, column=1)
root.mainloop()