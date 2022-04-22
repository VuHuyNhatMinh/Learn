import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, CURRENT

# Root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)

def value_changed():
    print(current_value.get())

current_value = tk.StringVar(value = 0)

spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=current_value,
    command=value_changed
)

spin_box.pack(fill=BOTH)

root.mainloop()