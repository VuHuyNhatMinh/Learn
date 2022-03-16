import tkinter as tk
from tkinter import PanedWindow, ttk
import os, time
      
class App(ttk.Frame):
    def __init__(self, parent):
        # super().__init__(parent)
        ttk.Frame.__init__(self)

        # Create the theme
        self.tk.call("source", "E:/Downloads/FPT/Semester3/Codes/azure.tcl")
        self.tk.call("set_theme", "dark")

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index = index, weight=1)
            self.rowconfigure(index = index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2" ]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]
        self.columns= ["Name", "File Extension", "Date modified"]

        # Create control variable
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value = True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value = 2)
        self.var_4 = tk.StringVar(value = self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value = 75.0)

        # Create widget
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the Checkbutton
        self.check_frame = ttk.LabelFrame(self, text = "Checkbuttons", padding = (20, 10))
        self.check_frame.grid(
            row = 0, column = 0, padx = (20, 10), pady = (20, 10), sticky = "nsew"
        )

        # Checkbuttons
        self.check_1 = ttk.Checkbutton(
            self.check_frame, text = "Unchecked", variable=self.var_0
        )
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.check_2 = ttk.Checkbutton(
            self.check_frame, text = "Checked", variable=self.var_1
        )
        self.check_2.grid(row=1, column=0, padx=5, pady= 10, sticky="nsew")

        self.check_3 = ttk.Checkbutton(
            self.check_frame, text = "Third state", variable=self.var_2
        )
        self.check_3.state(['alternate'])
        self.check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.check_4 = ttk.Checkbutton(
            self.check_frame, text = "Disabled", state = "disable"
        )
        self.check_4.state(['disabled !alternate'])
        self.check_4.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        ##########################################################
        
        # Separator
        self.separator = ttk.Separator(self)
        self.separator.grid(
            row = 1, column = 0, padx = (20, 10), pady = 10, sticky = "ew"
        )

        ##########################################################

        # Create a Frame for Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text = "Radiobuttons", padding = (20, 10))
        self.radio_frame.grid(
            row = 2, column = 0, padx = (20, 10), pady = 10, sticky = "nsew"
        )

        # Radiobuttons
        self.radio_1 = ttk.Radiobutton(
            self.radio_frame, text = "Unselected", variable = self.var_3, value = 1
        )
        self.radio_1.grid(row = 0, column = 0, padx = 5, pady = 10, sticky = "nsew")

        self.radio_2 = ttk.Radiobutton(
            self.radio_frame, text = "Selected", variable = self.var_3, value = 2
        )
        self.radio_2.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = "nsew")

        self.radio_3 = ttk.Radiobutton(
            self.radio_frame, text = "Disabled", state = "disabled"
        )
        self.radio_3.grid(row = 2, column = 0, padx = 5, pady = 10, sticky = "nsew")

        ##########################################################

        # Create a frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding = (0, 0, 0, 10))
        self.widgets_frame.grid(
            row = 0, column = 1, padx = 10, pady = (30, 10), sticky = "nsew", rowspan = 3
        )
        self.widgets_frame.columnconfigure(index = 0, weight = 1)

        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Entry")
        self.entry.grid(row = 0, column = 0, padx = 5, pady = (0, 10), sticky = "ew")
        
        # Spinbox
        self.spinbox = ttk.Spinbox(self.widgets_frame, from_ = 0,  to = 100, increment = 0.1)
        self.spinbox.insert(0, "Spinbox")
        self.spinbox.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = "ew")

        # Combobox
        self.combobox = ttk.Combobox(self.widgets_frame, values = self.combo_list)
        self.combobox.current(0)
        self.combobox.grid(row = 2, column = 0, padx = 5, pady = 10, sticky = "ew")

        # Read-only combobox
        self.readonly_combo = ttk.Combobox(
            self.widgets_frame, state = "readonly", values = self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row = 3, column = 0, padx = 5, pady = 10, sticky = "ew")

        # Menu for the Menubutton
        self.menu = tk.Menu(self)
        self.menu.add_command(label = "Menu item 1")
        self.menu.add_command(label = "Menu item 2")
        self.menu.add_separator()
        self.menu.add_command(label = "Menu item 3")
        self.menu.add_command(label = "Menu item 4")

        # Menubutton
        self.menubutton = ttk.Menubutton(
            self.widgets_frame, text = "Menubutton", menu = self.menu, direction = "below"
        )
        self.menubutton.grid(row = 4, column = 0, padx = 5, pady = 10, sticky = "ew")

        # OptionMenu: Drop Down Boxes
        self.optionmenu = ttk.OptionMenu(
            self.widgets_frame, self.var_4, *self.option_menu_list
        )
        self.optionmenu.grid(row = 5, column = 0, padx = 5, pady = 10, sticky = "ew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text = "Button")
        self.button.grid(row = 6, column = 0, padx = 5, pady = 10, sticky = "ew")

        # Accent button
        self.accentbutton = ttk.Button(
            self.widgets_frame, text = "Accent button", style = "Accent.TButton"
        )
        self.accentbutton.grid(row = 7, column = 0, padx = 5, pady = 10, sticky = "ew")

        # Toggle button
        self.togglebutton = ttk.Button(
            self.widgets_frame, text = "Toggle button", style = "Toggle.TButton"
        )
        self.togglebutton.grid(row = 8, column = 0, padx =5, pady = 10, sticky = "ew")

        # Switch 
        self.switch = ttk.Checkbutton(
            self.widgets_frame, text = "Switch", style = "Switch.TCheckbutton"
        )
        self.switch.grid(row = 9, column = 0, padx = 5, pady = 10, sticky = "ew")

        ##########################################################
        
        # Create a PaneWindow
        self.pw = PanedWindow(self, orient = "vertical")
        self.pw.grid(row = 0, column = 2, padx = (10, 0), pady = (20, 10), rowspan = 3, sticky = "nsew")

        # Create a Frame for treeview
        self.treeview_frame = ttk.Frame(self.pw)
        self.pw.add(self.treeview_frame)

        for index in [0, 1]:
            self.treeview_frame.columnconfigure(index = index, weight=1)
        
        self.treeview_frame.rowconfigure(index = index, weight=1)

        # Treeview
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns = self.columns, show = "headings"
        )
        self.treeview.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")

        # Define headings
        for column in self.columns:
            self.treeview.heading(column, text = column)
        
        # Generate treeview data
        path = os.getcwd()
        data = []
        entries = os.listdir(path)
        for file in entries:
            path_file = os.path.join(path, file)
            data.append((os.path.basename(path_file), os.path.splitext(file)[1][1:], time.ctime(os.path.getmtime(path_file)))) 
         
        # Add data to the treeview
        for data in data:
            self.treeview.insert('', tk.END ,values = data)
   
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.treeview_frame, command = self.treeview.yview)
        self.scrollbar.grid(row = 0, column= 1, padx = (0, 10), pady = 10, sticky= "nsew")
        self.treeview['yscrollcommand'] = self.scrollbar.set

        # Create a Frame for Notebook
        self.notebook_frame = ttk.Frame(self.pw)
        self.pw.add(self.notebook_frame)

        self.notebook_frame.columnconfigure(0, weight=1)
        self.notebook_frame.rowconfigure(0, weight=1)

        # Notebook
        self.notebook = ttk.Notebook(self.notebook_frame)
        self.notebook.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")

        # Tab 1
        self.tab_1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_1, text = "Tab 1")

        for index in [0, 1]:
            self.tab_1.columnconfigure(index = index, weight=1)
            self.tab_1.rowconfigure(index = index, weight=1)

         # Slider
        self.slider = ttk.Scale(self.tab_1, from_ = 0, to = 100, variable = self.var_5)
        self.slider.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")

        # Progressbar
        self.progressbar = ttk.Progressbar(
            self.tab_1, variable = self.var_5, mode = "determinate"
        )
        self.progressbar.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "ew")

        # Label 
        self.label = ttk.Label(self.tab_1, text = "Azure theme for ttk", justify = "center")
        self.label.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan = 2)

        # Tab 2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text = "Tab 2")

        # Tab 3 
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text = "Tab 3")

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.pack()
    root.mainloop() 