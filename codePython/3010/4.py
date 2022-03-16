from tkinter import *
from tkinter import ttk

root = Tk()
# root.resizable(False, False)
root.title("Scrollbar Widget Example")

# Apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Create the text widget
text = Text(root, height=10, wrap="none")
text.grid(row=0, column=0, sticky="EW")

# Create a scrollbar widget and set its command to the text widget
# scrollbar = ttk.Scrollbar(root, orient="vertical", command=text.xview)
# scrollbar.grid(row = 0, column=1, sticky="NS")

scrollbar = ttk.Scrollbar(root, orient="horizontal", command=text.xview)
scrollbar.grid(row = 0, column=0, sticky="SEW", )

# Communicate back to the scrollbar
# text["yscrollcommand"] = scrollbar.set
text["xscrollcommand"] = scrollbar.set

root.mainloop()