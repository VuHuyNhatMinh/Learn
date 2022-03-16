from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

# text.insert("10.1", "First position")
text.insert("10.0", "This is a Text Widget Demo")
root.mainloop()