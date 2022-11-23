import random, time
from threading import Event, Thread

event = Event()


def waiter(event):
    print("Start waiting...")
    event.wait()
    print("Continue executing...")
    event.clear()
    print("Waiter exit...")

def trigger(event):
    print("Start executing...")
    time.sleep(random.randrange(2, 5))
    event.set()
    print("Trigger exit...")


threads = []

# Cоздаём поток,который будет ожидать сигнала для продолжения выполнения работы

th = Thread(target=waiter, args=(event,))
threads.append(th)
th.start()

# Cоздаём поток, который будет сигнализировать о возможности продолжения работы

th = Thread(target=trigger, args=(event,))
threads.append(th)
th.start()

for thread in threads:
    thread.join()

print("All task executed successfully...")