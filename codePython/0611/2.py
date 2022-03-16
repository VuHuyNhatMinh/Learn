import tkinter as tk
from tkinter import Scrollbar, ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Treeview demo")
        self. geometry("620x200")

        self.tree = self.create_tree_widget()

    
    def create_tree_widget(self):
        columns = ('#1', '#2', '#3')
        tree = ttk.Treeview(self, columns = columns, show = "headings")

        # Define headings
        tree.heading("#1", text = "First Name")
        tree.heading("#2", text = "Last Name")
        tree.heading("#3", text = "Email")

        tree.bind("<<TreeviewSelect>>", self.item_selected)
        tree.grid(row = 0, column = 0, sticky = tk.NSEW)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient = tk.VERTICAL, command = tree.yview)
        tree.configure(yscroll = scrollbar.set)
        scrollbar.grid(row = 0, column = 1, sticky = "ns")

        # Generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first{n}', f'last{n}', f'email{n}@example.com'))

        # Add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values = contact)
        
        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # Show a message
            showinfo(title = "Information", message = ','.join(record))

if __name__ == '__main__':
    app = App()
    app.mainloop()
