from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Pack Demo")
root.geometry("300x200")

# Box 1
box1 = ttk.Button(
    root,
    text = "Box 1",
)

box1.pack(
    # fill = 'x',
    # fill = 'y',
    # expand=True
    ipadx=10,
    ipady=10
)

# Box 2
box2 = ttk.Button(
    root,
    text = "Box 2",
)

box2.pack(
    # fill = 'y',
    ipadx=10,
    ipady=10
)

root.mainloop()