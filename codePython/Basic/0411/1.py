import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("LabelFrame Demo")

# Label Frame
lf = ttk.LabelFrame(
    root, 
    text = "Alignment"
)

lf.grid(row=0, column=0, padx=20, pady=20)

alignment = tk.StringVar()

# Left radio Button
left_radio = ttk.Radiobutton(
    lf,
    text = "Left",
    value="left",
    variable=alignment
)

left_radio.grid(row=0, column=0, ipadx=10, ipady=10)

# Center radio button
center_radio = ttk.Radiobutton(
    root,
    text = "Center",
    value= "center",
    variable=alignment
)

center_radio.grid(row=0, column=1, ipadx=10, ipady=10)

# Right alignment radiobutton
right_radio = ttk.Radiobutton(
    root,
    text = "Right",
    value= "right",
    variable=alignment
)
right_radio.grid(row=0, column=2, ipadx=10, ipady=10)

root.mainloop()