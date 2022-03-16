import tkinter as tk
from tkinter import Menu

# Root window
root = tk.Tk()
root.title("Menu Demo")
root.geometry('300x300')

# Create a menubar
menubar = Menu(root)
root.config(menu = menubar)

# Create a menu
file_menu = Menu(menubar)

# Add a menu item to the menu
file_menu.add_command(
    label = "Exit",
    command = root.destroy,
)

# Add the File menu to the menubar
menubar.add_cascade(
    label = "File",
    menu = file_menu,
)

root.mainloop()