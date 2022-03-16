import tkinter 

master = tkinter.Tk()
# Set titile for the open window
master.title("place() method")
# Set the origin for the open window
master.geometry("450x350")

# Place: manage position and width of a window
button1 = tkinter.Button(master, text = "button1")
button1.place(x = 25, y = 100)

button2 = tkinter.Button(master, text = "button2")
button2.place(x = 100, y = 25)

button3 = tkinter.Button(master, text = "button3")
button3.place(x = 175, y = 100)

master.mainloop()