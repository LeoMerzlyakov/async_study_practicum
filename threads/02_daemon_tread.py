import time
from threading import Thread

'''
Обычно разработчики демонизируют те участки программы, 
которые должны регулярно выполнять какие-то фоновые задачи: 
например, утилиту cron или сервис, 
отвечающий за монтирование устройств.
'''

def custom_func(n, name):
    for i in range(n):
        print(f"From child {name} thread: {i}")
        time.sleep(0.5)


daemon_th = Thread(target=custom_func, args=(100, 'daemon'))
daemon_th.daemon = True
print("Start daemon")
daemon_th.start()
time.sleep(1)
print("Finish daemon")

th = Thread(target=custom_func, args=(10, 'nondaemon'))
th.start()
print("Start nondaemon")
time.sleep(1)
print("Finish nondaemon")


