import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Combobox Widget")

def month_changed(event):
    msg = f"You selected {month_cb.get()}!"
    showinfo(title="Result", message = msg)
 
# Month of year
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

label = ttk.Label(text = "Please select a month")
# label.pack(fill = 'x', padx=5, pady=5)
label.grid(row=0, column=0)
# Create a combobox
selected_month = tk.StringVar()

month_cb = ttk.Combobox(root, textvariable=selected_month)
# month_cb["values"] = months
# month_cb["state"] = "readonly"  # Normal
# month_cb.pack(fill = 'x', padx=5, pady=5)
month_cb.grid(row=1, column=0)
# month_cb.bind("<<ComboboxSelected>>", month_changed)

def click():
    e = tk.Label(root, text  = month_cb.get())
    e.grid(row = 4, column= 0)

button = tk.Button(root, command = click)
button.grid(row=3, column=0)

root.mainloop()