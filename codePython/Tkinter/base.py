from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New window Demo")
root.iconbitmap("icon.ico")

top = Toplevel()
top.title("Top window")
top.iconbitmap("icon.ico")

# lbl = Label(top, text="Hello World!").pack()
my_img = ImageTk.PhotoImage(Image.open("arrow.png"))
my_label = Label(top, image=my_img).pack()

root.mainloop()