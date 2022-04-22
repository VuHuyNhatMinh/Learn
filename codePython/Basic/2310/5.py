#app4.py
from tkinter import *

top = Tk()

top.geometry("400x250")

# Creating label 
uname = Label(top, text = "Username", underline = 0).place(x = 30, y = 50)

# Creating label
password = Label(top, text = "Password", cursor = "mouse").place(x = 30, y = 90)

sbmitbtn = Button(top, text = "Submit", activebackground = "pink", activeforeground  = "blue").place(x = 30, y = 120)
# from tkinter.ttk import *
# sbmitbtn = Button(top, text = "Submit").place(x = 30, y = 120)

e1 = Entry(top, width = 20).place(x = 100, y = 50)

e2 = Entry(top, width = 20).place(x = 100, y = 90)

top.mainloop()