from threading import Timer

work = 25
shortBreak = 10
longBreak = 20
timers, m = 0

def TakeBreak():
    timers += 1
    print("Time for a break!")
if timers == 3:
    m = longBreak
elif not timers % 2:
    m = shortBreak


t = Timer(m * 60, TakeBreak)
t.start()

t.join()