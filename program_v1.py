##Image Evaluator
#Ver. 1


# Imports
import random

from tkinter import *


#frame

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.button()

    def button(self):
        """Create's starting button"""
        Button(self,
               text = "Begin!",
               command = self.image_eval
               ).grid(row = 2, column = 2, sticky = W)

    def image_eval(self):
        Application()
        
        





#main
        
root = Tk()
root.title ("Image Evaluator")
root.geometry("400x150")
app = Application(root)
root.mainloop()





input("\n\nPress Enter to Exit")
