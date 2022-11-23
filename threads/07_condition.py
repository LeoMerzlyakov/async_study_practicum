import random
import time
from threading import Condition, Thread

condition = Condition()
data_pool = []

def producer(data_pool, pool_size):
    for i in range(pool_size):
        time.sleep(random.randrange(2, 5))

        # Блокируем потоки, подписанные на условие

        condition.acquire()
        num = random.randint(100, 500)
        data_pool.append(num)

        # Сигнализируем о возможности продолжить работу
        # При замене на .notify_all(), сигнал о продолжении получат все потоки,
        # подписанные и ожадающее текущий триггер

        condition.notify_all()
        print("Produced:", num)
        condition.release()
    print('producer ends')

def consumer(data_pool, pool_size):
    for i in range(pool_size):

        # Блокируем потоки, подписанные на условие

        condition.acquire()

        # Ожидание сигнала о возможности продолжения работы

        condition.wait()
        print("%s: Acquired: %s" % (time.ctime(), data_pool.pop()))
        condition.release()
    print('producer ends')


threads = []
threads_max = random.randrange(2, 7)

for func in [producer, consumer]:
    th = Thread(target=func, args=(data_pool, threads_max))
    threads.append(th)
    th.start()

for thread in threads:
    thread.join()

print("All task executed successfully...")
