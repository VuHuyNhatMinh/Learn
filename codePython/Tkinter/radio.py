from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button Demo")
root.iconbitmap("icon.ico")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text =text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel1 = Label(root, text=value)
    myLabel1.pack()

# r = IntVar()
# r.set("2")
# Radiobutton(root, text = "Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text = "Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
# myLabel1 = Label(root, text=r.get())
# myLabel1.pack()

# myButton = Button(root, text = "Clicked Me!", command=lambda: clicked(r.get())).pack()
myButton = Button(root, text = "Clicked Me!", command=lambda: clicked(pizza.get())).pack()

root.mainloop()