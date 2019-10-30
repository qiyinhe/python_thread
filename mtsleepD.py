# mtsleepD.py

import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc():
    '''可调用类'''
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print("Start loop %d at:" % nloop, ctime())
    sleep(nsec)
    print("Loop %d done at:" % nloop, ctime())

def main():
    print("Start at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)


    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at:", ctime())

if __name__ == '__main__':
    main()
