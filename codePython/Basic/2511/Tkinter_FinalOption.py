

import tkinter as tk
from tkinter import *
from tkinter import ttk


class createLabelFrame(ttk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.columnconfigure(0,weight=3)
        self._labelFrame_checkbutton()
    def _labelFrame_checkbutton(self):
        match_case = tk.StringVar()
        check = tk.StringVar()
        thirdstate = tk.StringVar()
        top_disable = tk.StringVar()
        #Top labelFrame
        top = ttk.LabelFrame(self,text="Checkbuttons")
        top.grid(column=0,row=0,sticky=tk.W)
        ttk.Checkbutton(top,text="Uncheck",variable=match_case,command=lambda:print(match_case.get())).grid(row=2,column=0,sticky=tk.W)
        ttk.Checkbutton(top,text="Check",variable=check,command=lambda:print(check.get())).grid(row=3,column=0,sticky=tk.W)
        ttk.Checkbutton(top,text="Thirdstate",variable=thirdstate,command=lambda:print(thirdstate.get())).grid(row=4,column=0,sticky=tk.W)
        ttk.Checkbutton(top,text="Disable",variable=top_disable,command=lambda:print(top_disable.get())).grid(row=5,column=0,sticky=tk.W)
        #ttk.Separator(top, orient='horizontal')
        # Separator
        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=0,  sticky="ew")

        # #Bot labelFrame
        bot = ttk.LabelFrame(self,text="Radiobuttons")
        bot.grid(column=0,row=6,sticky=tk.W)
        button =('Unselected','Selected','Disabled')
        select_radio = tk.StringVar()
        for i in button:
           r = ttk.Radiobutton(bot,text=i,variable=select_radio,value=i)
           r.grid(pady=1,padx=1,sticky=tk.W)

        separa = ttk.Separator(self, orient='horizontal')
        separa.grid(row=12,column=0,sticky=tk.W)

        for widget in self.winfo_children():#hàm chứa các widgets
            widget.grid(padx=10,pady=10)
    
class createInputWidget(ttk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.columnconfigure(0,weight=3)
        self._createWidget()
    def _createWidget(self):

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Create Entry
        entryWidget = ttk.Entry(self.widgets_frame)
        entryWidget.insert(0,"Entry")
        entryWidget.grid(column=1,row=0,sticky="w",pady=10)
        #create Spinbox
        spinboxWidget = ttk.Spinbox(self.widgets_frame,from_=-10,to=100,increment=1,wrap=True)
        spinboxWidget.insert(0,"SpinBox")
        spinboxWidget.grid(column=1,row=1,sticky="w",pady=10)
        #Combobox
        comboboxWidget = ttk.Combobox(self.widgets_frame)
        comboboxWidget.insert(0,"Combobox")
        comboboxWidget.grid(column=1,row=2,sticky="w",pady=10)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.columnconfigure(0,weight=4)
        self._build()
        # self.tk.call("source", "F:/Visual Code/Python/Azure-ttk-theme-main/azure.tcl")
        # self.tk.call("set_theme", "dark")
    def _build(self):
        self.labelFrame = createLabelFrame(self)
        self.labelFrame.grid(column=0,row=0,sticky="NSEW")
        self.createwidget = createInputWidget(self)
        self.createwidget.grid(column=1,row=0,sticky="NSEW")
if __name__ =="__main__":
    app = App()
    app.mainloop()
