from tkinter import *
from tkinter import ttk

def submit():
    file = open("Testfile.txt", "a")
    value = ("Question number:" + str(questionNumber.get()) + "\n" + "Question Stem :" + str(questionStem.get(1.0,END)) + "\n" + "Possible answers: " + "\n" + str(possibleAnswers.get(1.0, END)) + "\n" + "Correct Answer : " + str(correctAnswer.get()))
    if questionNumber.get() == "1":
        value = ("Test name : " + str(testname.get())  + "\n" + "Question number:" + str(questionNumber.get()) + "\n" + "Question Stem :" + str(questionStem.get(1.0,END)) + "\n" + "Possible answers: " + "\n" + str(possibleAnswers.get(1.0, END)) + "\n" + "Correct Answer: " + str(correctAnswer.get()))
    file.write(str(value))
    file.write("\n")
    file.close()
def clear():
    questionNumber.delete(0,END)
    questionStem.delete(1.0,END)
    possibleAnswers.delete(1.0, END)
    correctAnswer.delete(0,END)
    questionNumber.focus_set()
root = Tk()
root.geometry("700x450")
root.title("Question entry")
root.resizable(False, False)
root.configure(background= "Light Blue")

frame_heading = Frame(root)
frame_heading.grid(row = 0, column = 0, columnspan= 2, padx= 3, pady= 5)

frame_entry = Frame(root)
frame_entry.grid(row = 1, column= 0, columnspan= 2, padx= 25, pady= 10)

Label(frame_heading, text = "Name of Test", font = ("Ariel", 16)).grid(row = 0, column = 0, padx= 0, pady = 5)


Label(frame_entry, text = "Enter the question number : ").grid(row = 0, column = 0, padx= 10, pady = 5, sticky= E)
Label(frame_entry, text = "Enter the Stem: ").grid(row = 1, column = 0, padx= 10, pady =5, sticky= E)
Label(frame_entry, text = "Enter the 3 possible answers a, b and c :").grid(row = 2, column = 0, padx = 10, pady= 10)
Label(frame_entry, text = "Correct answer : ").grid(row = 3, column = 0 ,padx = 10, pady =10 )

testname = Entry(frame_heading, width = 30, font = ("Ariel", 16))
testname.grid(row = 0, column = 1, padx= 5, pady = 5)

questionNumber = Entry(frame_entry, width = 2, font = ("Ariel", 11))
questionNumber.grid(row = 0 , column = 1, padx =5 ,pady =5 ,sticky = W)

questionStem = Text(frame_entry, width = 50, height = 2, bg ="white", font = ("Ariel", 11))
questionStem.grid(row = 1, column = 1, padx =5, pady =5)

possibleAnswers = Text(frame_entry, width = 50, height = 10, bg = "white", font = ("Ariel", 11))
possibleAnswers.grid(row = 2, column= 1, padx = 5, pady = 5)

correctAnswer = ttk.Combobox(frame_entry, text = "a", font = ("Arial", 11))

correctAnswer.grid(row = 3, column = 1, padx =5, pady =5, sticky = W)
correctAnswer.config(values = ("a", "b", "c"))

submit_button = Button(root, text = "Submit", width = 7, command = submit)
submit_button.grid(row = 2, column = 0 , padx= 0, pady= 5)
clear_button = Button(root, text = "Clear", width = 7, command = clear)
clear_button.grid(row = 2, column = 1, padx= 0, pady= 5)



root.mainloop()