from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap("icon.ico")

# frame = LabelFrame(root, text = "This is my Frame...", padx=5, pady=5)
# frame = LabelFrame(root, text = "This is my Frame...", padx=50, pady=50)
frame = LabelFrame(root, padx=50, pady=50)

frame.pack(padx=10, pady=10)
# frame.pack(padx=100, pady=100)

b = Button(frame, text = "Click Me!")
# b.pack()
b.grid(row=0,column=0)

b2 = Button(frame, text = "Don't Click Me!")
b2.grid(row=1,column=1)

root.mainloop()