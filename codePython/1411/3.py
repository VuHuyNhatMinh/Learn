from tkinter import *

class Window(Frame):
    def __init__(self, master):
        #c1
        # Frame.__init__(self, master)
        # self.master = master
        #c2
        super().__init__(master)
        # self.master = master
        self.init_window()
        #c3
        # super(Frame, self).__init__(master)      
        # self.master = master  
        # self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.master.geometry('400x400') 

        # quitButton = Button(self.master, text='Quit')
        # quitButton.place(x=0, y=0)

root = Tk()
app = Window(root)
root.mainloop()