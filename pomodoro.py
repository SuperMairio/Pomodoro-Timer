from threading import Timer
from tkinter import *
import tkinter.messagebox

work = 25
shortBreak = 10
longBreak = 20
timers = 0
timeMin = 0
root=Tk()

def StartWork(timers):
    timers += 1
    timeMin = work
    message = "Time to get back to work!"

    tkinter.messagebox.showinfo('Pomodoro Timer',message)

    t = Timer(timeMin * 60, TakeBreak(timers))
    t.start()

def TakeBreak(timers):
    timers += 1
    message = "Time for a break!"

    tkinter.messagebox.showinfo('Pomodoro Timer',message)

    if timers == 3:
        timeMin = longBreak
    elif not timers % 2:
        timeMin = shortBreak

    t = Timer(timeMin * 60, StartWork(timers))
    t.start()

print("P O M O D O R O   T I M E R")
StartWork(timers)
t.join()
root.mainloop()