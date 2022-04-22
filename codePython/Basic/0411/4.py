import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Slider Demo")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Slider current value
current_value = tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    value_label.configure(text = get_current_value())

# Label for the slider
slider_label = ttk.Label(
    root, 
    text = "Slider"
)

slider_label.grid(row=0, column=0, sticky='W')

# Slider
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal", 
    command=slider_changed,
    tickinterval = 10,
    variable=current_value
)

slider.grid(row=0, column=1, sticky= "EW", columnspan=2)

# Current value Label
current_value_label = ttk.Label(root, text = "Current value: ")
current_value_label.grid(row=1, column=2, sticky="N", ipadx = 10, ipady= 10)

# Value Label
value_label = ttk.Label(root, text = get_current_value())

value_label.grid(row=2, column=2, sticky="N")
root.mainloop()
