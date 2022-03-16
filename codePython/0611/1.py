import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Create root window
root = tk.Tk()
root.title("Treeview Demo - Hierachical Data")
root.geometry("400x200")

# Configure the grid layout
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight= 1)

# Create a treeview
tree = ttk.Treeview(root)
tree.heading("#0", text="My Computer", anchor='w')

# Adding data
tree.insert('', tk.END, text='C', iid=0, open=False)
tree.insert('', tk.END, text='D', iid=1, open=False)
tree.insert('', tk.END, text='E', iid=2, open=False)
tree.insert('', tk.END, text='F', iid=3, open=False)
tree.insert('', tk.END, text='G', iid=4, open=False)

# Adding children of first node
tree.insert('', tk.END, text="User", iid=5, open=False)
tree.insert('', tk.END, text="Program File", iid=6, open=False)
tree.insert(5, tk.END, text="Program Data", iid=8, open=False)
tree.insert(6, tk.END, text="Program Data1", iid=9, open=False)

tree.move(5, 0, 0)
tree.move(6, 0, 1)
# tree.move(8, 5, 1)
tree.move(8, 5, 0)

tree.move(9, 8, 0)

# Place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky="NSEW")

# Run the app
root.mainloop()