from tkinter import *
window = Tk()
window.geometry("200x120")
window.configure(background= "Light Green")
label = Label(window)
def Right():
    label.configure(text = "Right")
    label.grid(row = 1, column = 1, padx = 20, pady = 10, sticky= E)
def Left():
    label.configure(text = "Left")
    label.grid(row = 1 ,column = 0, padx =20, pady = 10, sticky = W)
right = Button(window, text = "Right", width = 5, command = Right).grid(row = 0, column = 1, padx = 20, pady = 20)
left = Button(window, text = "Left", width = 5, command = Left).grid(row = 0, column = 0, padx = 20, pady = 20)
window.mainloop()