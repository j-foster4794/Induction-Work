#-------------------------------------------------------------------------------
# Name:       A Level Induction Coding Project
# Purpose:
#
# Author:      James F
#
# Created:     14/08/2023
# Copyright:   (c) Wooki 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
Window = Tk()
Window.title("Placing a button")
def response():
    Label(Window, text = "Hi there!").pack()
button = Button(Window, text = "Click here",  command = response)
button.pack()
Window.mainloop()
