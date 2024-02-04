from tkinter import *
window = Tk()
window.configure(background = "Light Green")
window.geometry("200x120")
def Left():
    Label(window, text = "Left").grid(row =  1, column = 0, columnspan = 3, padx = 20, pady = 10,)
def Right():
    Label(window, text = "Right").grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 10)
Left = Button(window, text = "Left", width = 6, command = Left)
Left.grid(row = 0, column = 0, padx = 20, pady = 20)
Right = Button(window, text = "Right", width = 6 ,command = Right)
Right.grid(row = 0, column = 1, padx = 20, pady = 20)



window.mainloop()