from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep


participants = ["Boris", "Oleg", "Slava", "Peter"]
threads_count = len(participants)
b = Barrier(threads_count)

def start_game():
    player = participants.pop()
    sleeping_time = randrange(2, 10)
    print("Player {} started: {}".format(player, sleeping_time))
    sleep(sleeping_time)
    print("Player {} waiting: {}".format(player, sleeping_time))
    b.wait()
    print("Player {} finished at: {}".format(player, ctime()))


threads = []
print("Starting game...")

for i in range(threads_count):
    th = Thread(target=start_game)
    threads.append(th)
    th.start()

for thread in threads:
    thread.join()

print("Game finished")
