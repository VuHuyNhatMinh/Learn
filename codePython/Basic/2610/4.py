from tkinter import *
from tkinter import ttk

# Creating Tk window
master = Tk()

# Creating a Fra, e which can expand according to the size
# of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand= True)

# Button widgets which can also expand and fill in the parent
# widget entirely 
# Button1
b1 = ttk.Button(pane, text = "Click Me!")
b1.pack(side = TOP, expand= True, fill = BOTH)

# Button3
b3 = Button(pane, text = "I'm also button", command= master.destroy)
b3.pack(side = TOP, expand= True, fill = BOTH)

# Button2
b2 = ttk.Button(pane, text = "Click me too")
b2.pack(side = TOP, expand= True, fill = BOTH)

master.mainloop()