# mpsleepF.py

from multiprocessing import Pool
from time import sleep, ctime
import os

loops = [4, 2, 3, 4, 5, 2, 1]

def loop(nsec):
    print("[%s] %s start." % (ctime(), os.getpid()))
    sleep(nsec)
    print("[%s] %s end." % (ctime(), os.getpid()))

def main():
    print("[%s] %s main process start ... ..." % (ctime(), os.getpid()))
    p = Pool(processes=3)

    rl = p.map(loop, loops)
    p.close()
    p.join()

    print("[%s] %s main process end ... ..." % (ctime(), os.getpid()))

if __name__ == '__main__':
    main()
