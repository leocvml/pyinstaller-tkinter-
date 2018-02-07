from tkinter import Tk, Label, Button

import numpy as np
import os
 
import base64
from icon import img
 
class GUI:

    def __init__(self, master):
        self.master = master
        master.title("hello_world")
        master.minsize(width=800, height=300)
        master.maxsize(width=400, height=300)

        self.button0 = Button(master, text="1. show_img", width=40, command=self.show)
        self.button0.grid(row=0, column=0)

    def show(self):
         print('hello')


            

root = Tk()
my_gui = GUI(root)
tmp = open("temp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("temp.ico")
os.remove("temp.ico")
root.mainloop()
