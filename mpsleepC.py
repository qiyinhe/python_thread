# mpsleepC.py

from multiprocessing import Process
from time import sleep, ctime
import os

loops = [4, 2]

def loop(nsec):
    print("[%s] %s start." % (ctime(), os.getpid()))
    sleep(nsec)
    print("[%s] %s end." % (ctime(), os.getpid()))

def main():
    print("[%s] %s main process start ... ..." % (ctime(), os.getpid()))
    processes = []
    nloops = range(len(loops))

    for i in nloops:
        t = Process(target=loop, args=(loops[i], ))
        processes.append(t)


    for i in nloops:
        processes[i].start()

    for i in nloops:
        processes[i].join()

    print("[%s] %s main process end ... ..." % (ctime(), os.getpid()))

if __name__ == '__main__':
    main()
