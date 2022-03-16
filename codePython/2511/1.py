import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Demo")
        self.geometry("300x300")

        # Menubutton variable        
        self.selected_color = tk.StringVar()
        self.selected_color.trace('w', self.menu_item_selected)
        
        # Create the menu button
        self.create_menu_button()
    
    def menu_item_selected(self, *args):
        ''' Handle menu selected event '''
        self.config(bg = self.selected_color.get())
  
    def create_menu_button(self):
        ''' Create a menu button '''
        # Menu variable
        colors = ('Red', 'Green', 'Blue')

        # Create the Menubutton
        menu_button = ttk.Menubutton(
            self, 
            text = 'Select a color'
        )    

        # Create a new menu instance
        menu = tk.Menu(menu_button, tearoff = 0)

        for color in colors:
            menu.add_radiobutton(
                label = color,
                value = color,
                variable = self.selected_color,
                # command = lambda: print(self.selected_color.get())
            )
        
        # Associate menu with the Menubutton
        menu_button['menu'] = menu

        menu_button.pack(expand = True)

if __name__ == '__main__':
    app = App()
    app.mainloop()