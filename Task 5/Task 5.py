from tkinter import *
from tkinter import messagebox
window = Tk()
def accept():
    messagebox.showinfo(title = "Accepted", message = "Password is accepted")
def reject():
    messagebox.showinfo(title = "Rejected", message = "Password is rejected as it is not long enough")
def Submit():
    p = password.get()
    if len(p) >= 6:
        accept()
    else:
        reject()
        username.delete(0, END)
        password.delete(0, END)
def Clear():
    username.delete(0, END)
    password.delete(0, END)
window.geometry("240x200")
window.configure(bg= "Light Blue")
window.title("Detail Entry")
heading = Frame(window)
heading.grid(column= 0, row = 0, padx= 40, pady = 5)
Label(heading, text = "Enter Chosen Details").grid(column = 0, row = 0, columnspan = 2, padx = 15, pady = 5)
entry = Frame(window)
entry.grid(column = 0, row = 1, padx = 20, pady =5)
username = Entry(entry)
username.grid(column = 1, row = 0, padx = 5, pady = 5)
Label(entry,text = "Username : ").grid(column = 0, row = 0, padx = 5, pady = 5)
password = Entry(entry)
password.grid(column = 1, row = 1, padx =5 , pady =5)
Label(entry, text = "Password : ").grid(column = 0, row = 1, padx = 5, pady =5)
buttons = Frame(window)
buttons.grid(row = 2, column = 0, padx = 20, pady = 20)
submit = Button(buttons, text = "Submit", command = Submit)
clear = Button(buttons, text = "Clear", command = Clear)
submit.grid(column = 0, row = 0, padx = 5, pady = 5)
clear.grid(column = 1, row = 0, padx =5, pady =5)
window.mainloop()