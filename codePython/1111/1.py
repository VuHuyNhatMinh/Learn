import tkinter as tk
from tkinter import Button, ttk

def main():
    root = tk.Tk()
    root.geometry("200x100")

    root.tk.call("source", "E:/Downloads/FPT/Semester3/Codes/azure.tcl")
    root.tk.call("set_theme", "light")

    Button1 = ttk.Button(root, text = "Button1")
    Button1.pack()

    Button2 = ttk.Button(root, text = "Button2")
    Button2.pack()

    Button3 = ttk.Button(root, text = "Button3")
    Button3.pack()

    root.mainloop()

if __name__ == '__main__':
    main()