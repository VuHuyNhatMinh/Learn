# Importing everything from tkinter module
from tkinter import *
from tkinter import ttk

# Main tkinter window
root = Tk()

# Panewindow object
pw = PanedWindow(orient = 'vertical')

# Button Widget
top = ttk.Button(pw, text = "Click Me! \nI'm a Button")
top.pack(side = TOP)

# This will add button widget to the panewindow
pw.add(top)

# Checkbutton Widget
bot = Checkbutton(pw, text = "Choose Me!")
bot.pack(side = TOP)

# This will add Checkbutton to panewindow
pw.add(bot)

pw.pack(fill = BOTH, expand = TRUE)

# This method is used to show sash
pw.configure(sashrelief = RAISED)

# Infinite loop can be destroyed by 
# keyboard or mouse interrupt
mainloop()