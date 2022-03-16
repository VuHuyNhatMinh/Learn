# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# text = tk.StringVar()
# textbox = ttk.Entry(root, textvariable=text)
# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.geometry("400x400")
# text = StringVar()
# textbox = ttk.Entry(root, textvariable=text.get())
# textbox.place(x = 175, y = 100)
# textbox.pack()

# textbox.get()
# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("300x200")
text = StringVar()

textbox = Entry(root, textvariable= text)
textbox.place(x = 100, y = 100)
textbox.pack()

textbox1 = Entry(root, text= text)
textbox1.place(x = 100, y = 300)
textbox1.pack()

root.mainloop()