import time
import os
import multiprocessing as mp



def printer(a: str):
    time.sleep(50)
    print(f'Done! Argument {a}')
    
if __name__ == '__main__':
    mp.set_start_method('spawn')
    p = mp.Process(target=printer, args=('arg_1',))
    p.start()
    print('Пока выполняется процесс, съешьте ещё этих мягких французских булок да выпейте же чаю ☕')
    
    print(f'Main pid: {os.getpid()}')
    print(f'Slave pid: {p.pid}')
    
    p.join()