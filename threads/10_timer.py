from threading import Timer
import random


def logger(msg):
    print(f"Logging info: {msg}")


def reject(timer):
    timer.cancel()
    print("Cancelled timer...")


delay = random.randrange(5, 7)
timer1 = Timer(interval=delay, function=logger, args=(f"Starting func after {delay} s delay...",))
timer1.start()

timer2 = Timer(interval=3, function=logger, args=("Second timer with message",))
timer2.start()

rejecter = Timer(interval=2, function=reject, args=(timer2,))
rejecter.start()

print("Program finished...")