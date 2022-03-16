from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def openfilename():
    filename = filedialog.askopenfilename(title = '"pen')
    return filename

def open_img():
    x = openfilename()

    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)

    img = ImageTk.PhotoImage(img)
    panel = Label(root, image = img)

    panel.image = img
    panel.grid(row = 2)

root = Tk()
root.title("Image test")
root.geometry("550x300")
root.resizable(width = True, height = True)
btn = Button(root, text = 'open image', command = open_img).grid(row = 1, columnspan = 4)

root.mainloop()
