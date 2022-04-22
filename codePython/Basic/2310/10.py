from tkinter import *
from tkinter import ttk

# Create Object 
root = Tk()

# Set geometry (widthxheight)
root.geometry("400x400")

# This will create style object
style = ttk.Style()

# This will be adding style, and naming that style variable as W.Tbutton
# (TButton is used for ttk.Button: all button)
style.configure("minhvhn.TButton", font = ("calibri", 40, "bold", "underline"), foreground = "red")

# Style will be reflected only on this button because we are providing style
# only on this Button

''' Button 1 '''
btn1 = ttk.Button(root, text = "Quit !", style = "minhvhn.TButton", command = root.destroy)
btn1.grid(row = 0, column = 3, padx = 100)

''' Button 2 '''
btn2 = ttk.Button(root, text = "Click me!", command = None)
btn2.grid(row = 1, column=3, padx= 100, pady= 10)

root.mainloop()