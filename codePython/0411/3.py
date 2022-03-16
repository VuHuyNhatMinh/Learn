import tkinter as tk
from tkinter import ttk
from tkinter.constants import SOLID
from types import SimpleNamespace

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Combobox Widget")

slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient="vertical",   # Horizontal,
)

slider.grid(row=0, column=0)

current_value = tk.DoubleVar()
slider_1 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    variable=current_value
)
slider_1.grid(row = 0, column= 1)
root.mainloop()