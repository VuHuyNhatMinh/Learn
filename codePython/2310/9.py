from tkinter import *
from tkinter import ttk

master = Tk()

master.geometry("200x200")

b1 = Button(master, text = "Click me !")
b1.place(x = 180, y = 2)

# Label widget 
l = Label(master, text = "I'm a Label")
l.place(anchor = NW)

# Button widget
b2 = Button(master, text = "Done")
b2.place(relx = 0.7, rely = 0.7)

button2 = Button(master, text = "button2")
button2.place(x = 100, y = 25)

button3 = Button(master, text = "button3")
button3.place(x = -2, y = 100)

button4 = Button(master, text = "button4")
button4.place(relheight=0.3, relwidth=0.3)

button5 = Button(master, text = "button5")
button5.place(x = 175, y = 100)

photo = PhotoImage(file = r"arrow.png")
photoimage = photo.subsample(10)

button4 = ttk.Button(master, text = "button4", image = photo)
button4.place(relheight = 0.3, relwidth = 0.3)
master.mainloop()