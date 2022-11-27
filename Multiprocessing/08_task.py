import multiprocessing as mp
from multiprocessing import Process, Queue


class Worker(Process):
    def __init__(self, func, func_args, queue):
        # Инициализация переменных
        self.queue = queue
        self.func = func
        self.func_args = func_args

    def run(self):
        # Вызов передаваемого метода и заполнение очереди
        result = self.func(**self.func_args)
        self.queue.put(result)
        return result
        
        
def foo(a):
    return f'aaa {a}'
        
if __name__ == '__main__':
    queue = Queue()
    w = Worker(foo, {'a': '1234' }, queue)
    w.run()
    print(queue.get())