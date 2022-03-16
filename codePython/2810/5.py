import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
# root.geometry("500x200")
root.title("Replace")
root.resizable(0,0)

# Label
label_find = ttk.Label(root, text = "Find what: ")
label_find.grid(column = 0, row = 0, sticky = tk.EW, padx = 5, pady = 5)

label_replace = ttk.Label(root, text = "Replace with: ")
label_replace.grid(column = 0, row = 1, sticky = tk.EW, padx = 5, pady = 5)

# Entry
entry_find = ttk.Entry(root)
entry_find.grid(column = 1, row = 0, sticky = tk.EW, padx = 5, pady = 5)

entry_replace = ttk.Entry(root)
entry_replace.grid(column = 1, row = 1, sticky = tk.EW, padx = 5, pady = 5)

# Button
button_find_next = ttk.Button(root, text = "Find Next")
button_find_next.grid(column = 2, row = 0, sticky = tk.EW, padx = 5, pady = 5)

button_replace = ttk.Button(root, text = "Replace")
button_replace.grid(column = 2, row = 1, sticky = tk.EW, padx = 5, pady = 5)

button_replace_all = ttk.Button(root, text = "Replace All")
button_replace_all.grid(column = 2, row = 2, sticky = tk.EW, padx = 5, pady = 5)

button_cancel = ttk.Button(root, text = "Cancel")
button_cancel.grid(column = 2, row = 3, sticky = tk.EW, padx = 5, pady = 5)

button_match_case = ttk.Button(root, text = "Match case")
button_match_case.grid(column = 0, row = 2, sticky = tk.EW, padx = 5, pady = 5)

button_wrap_around = ttk.Button(root, text = "Wrap around")
button_wrap_around.grid(column = 0, row = 3, sticky = tk.EW, padx = 5, pady = 5)

root.mainloop() 