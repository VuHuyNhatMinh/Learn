# mainloop()?

from tkinter import *
root = Tk()
password = StringVar()

password_entry = Entry(
    root, 
    textvariable=password,
    show='*'
)

password_entry.pack()
root.mainloop()
