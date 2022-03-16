from tkinter import *

root = Tk()
root.geometry("200x300")
root.title("Main")

l = Label(root, text = "This is root window")

top = Toplevel()
top.geometry("180x100")
top.title("toplevel")
l2 = Label(top, text = "This is toplevel window")

l.pack()
l2.pack()

top.mainloop()