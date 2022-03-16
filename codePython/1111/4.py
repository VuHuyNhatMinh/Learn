from tkinter import *
from tkinter import messagebox

# Object of Tk()
main = Tk()

# Function to use the askquestion() function
def Submit():
    messagebox.askquestion("Form", 
                            "Do you want to Submit?")

# Setting geometry of window instance
main.geometry("100x100")

# Creating window
B1 = Button(main, text = "Submit", command = Submit)

# Button positioning
B1.pack()

# Infinite loop till close
main.mainloop()