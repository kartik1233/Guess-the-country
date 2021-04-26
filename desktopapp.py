import tkinter

from tkinter import *
from tkinter import messagebox
import random

from random import shuffle


window = Tk()

window.geometry('300x300')
window.configure(background='#242B2E')
window.title("JumbleBot")
window.iconbitmap("games.ico")
label = Label(window, font='times 20')
label.pack(pady='30', ipady='10', ipadx='10')

answers = ["America", "India", "Australia", "France", "China", "Srilanka", "Russia"]
questions = []
for i in answers:
    word = list(i)
    shuffle(word)
    questions.append(word)
num = random.randint(0, len(questions)-1)

def initial():
    global questions, num
    label.configure(text=questions[num])

def checkanswers():
    global questions, num, answers
    user_input = e1.get()
    if user_input == answers[num]:
        messagebox.showinfo('success', 'you got it right!!')
        resetswitch()
    else:
        messagebox.showinfo('Error', 'Your answer is wrong!!')
        e1.delete(0, END)

def resetswitch():
    global questions , answers, num
    num = random.randint(0, len(questions)-1)
    label.configure(text=questions[num])
    e1.delete(0, END)


answer = StringVar()
e1 = Entry(window, textvariable=answer)
e1.pack(ipady='5', ipadx='5')

button1 = Button(window, text="check", width='20', command=checkanswers, bg='#B4161B')
button1.pack(pady=40)
button2 = Button(window, text="Reset", width='20', command=resetswitch, bg='#CAD5E2')
button2.pack()


initial()


window.mainloop()


