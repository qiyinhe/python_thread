# mpsleepE.py

import multiprocessing
import os
from time import sleep, ctime

loops = [4, 2]

class MyProcess(multiprocessing.Process):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nsec):
    print("[%s] %s start." % (ctime(), os.getpid()))
    sleep(nsec)
    print("[%s] %s end." % (ctime(), os.getpid()))

def main():
    print("[%s] %s main process start ... ..." % (ctime(), os.getpid()))
    processes = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyProcess(loop, (loops[i], ), loop.__name__)
        processes.append(t)

    for i in nloops:
        processes[i].start()

    for i in nloops:
        processes[i].join()

    print("[%s] %s main process end ... ..." % (ctime(), os.getpid()))

if __name__ == '__main__':
    main()
