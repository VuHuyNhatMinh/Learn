from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button!")
    myLabel.pack()

# myButton = Button(root, text = "Click Me!", state=DISABLEx`D, padx=50, pady=50)
# red, blue,...: colour can be in hex.
# Using function but do not hvae (): command = myClick() is false.
myButton = Button(root, text = "Click Me!", command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()