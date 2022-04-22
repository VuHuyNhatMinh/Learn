import tkinter as tk
from tkinter import Message, ttk
from typing import Container
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Checkbox Widget Demo")

checkbox_var = tk.StringVar()

def check_changed():
    # print("Checked")
    msg = f"You checked"
    showinfo(
        title = "Inf",
        message=msg
    )

checkbox = ttk.Checkbutton(root, text = "<checkbox label>", command=check_changed, variable=checkbox_var, 
                            onvalue="<value_when_checked>", offvalue="<value_when_unchecked>")
# checkbox = ttk.Checkbutton(root, text = "<checkbox label>", command=check_changed, variable=checkbox_var, 
#                             onvalue=1, offvalue=0)

checkbox.pack()

root.mainloop()