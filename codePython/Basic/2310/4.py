from tkinter import *
from tkinter import messagebox

maintk = Tk()
maintk.geometry("400x200")

def clickRedButton():
    messagebox.showinfo("Hello", "Red Button clicked")

def clickBlueButton():
    messagebox.showinfo("Hello", "Blue Button clicked")

def main():
    b1 = Button(maintk, text = "Red", command = clickRedButton, activeforeground = "red", activebackground = "pink", pady = 10)
    b2 = Button(maintk, text = "Blue", command = clickBlueButton, activeforeground = "blue", activebackground = "pink", pady = 10)
    b3 = Button(maintk, text = "Green", activebackground = "green", activeforeground = "pink", pady = 10)
    b4 = Button(maintk, text = "Yellow", activeforeground = "yellow", activebackground = "pink", pady = 10)
    b5 = Button(maintk, text = "red", activebackground = "green", activeforeground = "pink", pady = 10)
    b1.pack(side = LEFT)
    b2.pack(side = RIGHT)
    b3.pack(side = TOP)
    b4.pack(side = BOTTOM)
    # b5.pack(side = CENTER)
    maintk.mainloop()

if __name__ == "__main__":
    main()