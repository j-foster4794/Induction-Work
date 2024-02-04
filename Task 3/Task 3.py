from tkinter import *
def submit():
    print("Username", username.get())
    print("First name", firstname.get())
    print("Surname", surname.get())
    list = []
    list.append(username.get())
    list.append(firstname.get())
    list.append(surname.get())
    student_details = open("Details3.txt", "a")
    student_details.write(str(list))
    student_details.write("\n")
    student_details.close()
def clear():
    username.delete(0,END)
    firstname.delete(0,END)
    surname.delete(0,END)
    username.focus_set()
root = Tk()
root.geometry("270x240")
root.title("Student Details")
root.resizable(False,False)
root.configure(background= "Light Blue")

frame_heading = Frame(root)
frame_heading.grid(row = 0, column = 0, columnspan = 2, padx = 30, pady = 5)

frame_entry = Frame(root)
frame_entry.grid(row = 1, column = 0, columnspan = 2, padx = 25, pady = 10)

Label(frame_heading, text = "Student details form", font = ("Comic Sans", 16)).grid(row = 0, column = 0, padx = 0, pady = 5)

Label(frame_entry, text = "Username: ").grid(row = 0, column = 0, padx= 10 , pady = 5)
Label(frame_entry, text = "First Name: ").grid(row =1, column = 0, padx = 10, pady = 10)
Label(frame_entry, text = "Surname: ").grid(row =2, column= 0, padx= 10, pady = 10)

username = Entry(frame_entry, width = 15, bg = "white")
username.grid(row = 0, column = 1, padx = 5, pady = 5)

firstname = Entry(frame_entry, width = 15, bg = "white")
firstname.grid(row = 1, column =1, padx = 5, pady = 5)

surname = Entry(frame_entry, width = 15, bg = "white")
surname.grid(row = 2, column =1, padx = 5, pady = 5)

submit_button = Button(root, text = "Submit", width = 7, command = submit)
submit_button.grid(row = 2, column = 0, padx = 0, pady = 5)

clear_button = Button(root, text = "Clear", width = 7, command = clear)
clear_button.grid(row = 2, column = 1, padx = 0, pady = 5)




root.mainloop()
