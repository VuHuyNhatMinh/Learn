import tkinter as tk
from tkinter import ttk

class CollapsiblePane(ttk.Frame):
    '''
    ---USAGE---
    collapsiblePane = Collaspible(parent, expanded_text = [string],
                                 collapsed_text = [string])
    collapsiblePane.pack()
    button = Button(collapsiblePane.frame).pack()
    '''

    def __init__(self, parent, expanded_text = "Collapse <<", 
                 collapsed_text = 'Expand >>'):
        
        ttk.Frame.__init__(self, parent)

        # These are the class variable
        # see a underscope in expanded_text and _collapsed_text
        # this means these are private to class
        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text

        # Here weight implies that it can grow it's
        # size if extra space is available
        # default weight is 0
        self.columnconfigure(1, weight = 1)

        # Tkinter variable storing integer value
        self._variable = tk.IntVar()

        # Checkbutton is created but will behave as Button
        # cause in style, Buttons is passed
        # main reason to do this is Button do not support
        # variable option but checkbutton do
        self._button = ttk.Checkbutton(self, variable = self._variable,)