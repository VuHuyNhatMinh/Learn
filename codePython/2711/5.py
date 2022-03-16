from tkinter import *
from tkinter.ttk import *

master = Tk()

# p1 = PhotoImage(file = 'info.png')

# Setting icon of master window
# master.iconphoto(False, p1)

master.iconphoto(False, 'info.png')

# Creating button
b = Button(master, text = 'Click me!')
b.pack(side = TOP)

master.mainloop()