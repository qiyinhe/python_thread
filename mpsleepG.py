# mpsleepG.py

from multiprocessing import Pool
from time import sleep, ctime
import os

loops = [4, 2, 3, 4, 5, 2, 1]

def loop(nsec):
    print("[%s] %s start." % (ctime(), os.getpid()))
    sleep(nsec)
    print("[%s] %s end." % (ctime(), os.getpid()))

def main1():
    print("[%s] %s main process_1 start ... ..." % (ctime(), os.getpid()))
    p = Pool(processes=3)

    for i in range(len(loops)):
        p.apply(loop, (loops[i], ))

    p.close()
    p.join()

    print("[%s] %s main process_1 end ... ..." % (ctime(), os.getpid()))

def main2():
    print("[%s] %s main process_2 start ... ..." % (ctime(), os.getpid()))
    p = Pool(processes=3)

    for i in range(len(loops)):
        p.apply_async(loop, (loops[i], ))

    p.close()
    p.join()

    print("[%s] %s main process_2 end ... ..." % (ctime(), os.getpid()))

if __name__ == '__main__':
    main1()
    main2()
