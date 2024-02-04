from tkinter import *
window = Tk()
window.geometry("240x140")
window.resizable(False, False)
window.title("Student Details Search")
window.configure(background= "White")
def search():
    item = username.get()
    Found = False
    details = open("details4.txt", "r")
    list = details.readlines()
    for i in range(len(list)):
        newlist = list[i].split()
        if newlist[0] == item:
            print("Username : " + newlist[0] + "\n" + "First Name : " + newlist[1] + "\n" + "Surname : " + newlist[2] )
            Found = True
    if Found == False:
        print("No student using this username was found in the data base.")
def clear():
    username.delete(0, END)
Label(window, text = "Student Details Search", background= "light blue").grid(column = 0, row = 0, padx = 60, pady = 5)
entry = Frame(window)
entry.grid(column = 0, row = 1, padx = 5, pady = 5)
Label(entry, text = "Enter username :").grid(row = 0, column = 0, padx = 10 , pady = 10)
username = Entry(entry, width = 15, bg = "Light Blue")
username.grid(row = 0, column = 1, padx = 3, pady = 10)
s = Button(entry, text = "Search", command = search)
s.grid(row = 1, column = 0, pady = 5)
c = Button(entry, text = "Clear", command = clear)
c.grid(row = 1, column = 1, pady = 5)
window.mainloop()