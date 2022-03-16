import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()

root.geometry("240x100")
root.title("Login")
root.resizable(0,0)

class Login:
    def __init__(self, master):
        # Username
        self.username_label = ttk.Label(root, text = "Username: ")
        self.username_label.grid(column = 0, row = 0, sticky = tk.W, padx = 5, pady = 5)

        self.username_entry = ttk.Entry(root)
        self.username_entry.grid(column = 1, row = 0, sticky = tk.W, padx = 5, pady = 5)

        # Password
        self.password_label = ttk.Label(root, text = "Password: ")
        self.password_label.grid(column = 0, row = 1, sticky = tk.W, padx = 5, pady = 5)

        self.password_entry = ttk.Entry(root, show = '*')
        self.password_entry.grid(column = 1, row = 1, sticky = tk.W, padx = 5, pady = 5)

        # Login button
        self.login_button = ttk.Button(root, text = "Login")
        self.login_button.grid(column = 1, row = 3, sticky = tk.E, padx = 5, pady = 5)

l = Login(root)
root.mainloop()