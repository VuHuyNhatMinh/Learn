from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
# root.iconbitmap('@images.xbm')
img = PhotoImage(file='arrow.png')
root.iconphoto(True, img)   # Expand to see the icon


my_img = ImageTk.PhotoImage(Image.open("arrow.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text = "Exit", command=root.quit)
button_quit.pack()
root.mainloop()