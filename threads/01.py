import threading
import time


def thread_func(*args):
    thread_name = threading.current_thread().name
    print(f'Поток {thread_name} запустился')
    time.sleep(3)
    print(f'Поток {thread_name} завершился')


# Создание потока
x = threading.Thread(target=thread_func, name="my-thread")
# Запуск потока
x.start()
print("Программа завершена")