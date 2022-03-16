from tkinter import *

root = Tk()

root.title("Pack Demo")

button_1 = Button(root, text = "Box 1", fg = "white", bg = "red")
button_1.pack(side = TOP, fill = 'x', expand= True)

button_2 = Button(root, text = "Box 2", fg = "white", bg = "green")
button_2.pack(side = TOP, fill = 'x', expand= True)

button_3 = Button(root, text = "Box 3", fg = "white", bg = "blue")
button_3.pack(side = TOP, fill = 'x', expand= True)

button_left = Button(root, text = "Left", fg = "black", bg = "cyan")
button_left.pack(side = LEFT, fill = 'y', expand= True)

button_center = Button(root, text = "Center", fg = "black", bg = "violet")
button_center.pack(side = LEFT, fill = 'y', expand= True)

button_right = Button(root, text = "Right", fg = "black", bg = "yellow")
button_right.pack(side = LEFT, fill = 'y', expand= True)

root.mainloop()
