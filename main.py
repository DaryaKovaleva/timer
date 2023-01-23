from tkinter import *
from playsound import playsound
import time

class Timer:
    def __init__(self):
        self.root = Tk()
        self.root.title('Timer')
        self.root.geometry('350x300+100+100')
        self.title = Label(
            self.root,
            text='Timer',
            font=('Arial 16 bold'),
            bg='brown',
            fg='#FF0')
        self.title.place(x = 150, y = 10)

        self.hours = StringVar(self.root)
        self.hours_inp = Entry(self.root, textvariable=self.hours)
        self.minutes = StringVar(self.root)
        self.minutes_inp = Entry(self.root, textvariable=self.minutes)
        self.seconds = StringVar(self.root)
        self.seconds_inp = Entry(self.root, textvariable=self.seconds)
        self.hours_inp.place(x = 60, y = 150)

        self.start = Button(self.root, text='start', font=('Arial', 12), bg='white')
        self.stop = Button(self.root, text='stop', font=('Arial', 12), bg='white')

        self.start.place(x = 100, y = 200)
        self.stop.place(x = 200, y = 200)

        self.root.mainloop()
n = Timer()