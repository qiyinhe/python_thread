# zombie_process.py

import multiprocessing
from time import ctime, sleep
import os

def demo():
    print('[%s] %s start.' % (ctime(), os.getpid()))
    sleep(1)
    print('[%s] %s end.' % (ctime(), os.getpid()))

def main():
    print('[%s] %s father process start ... ...' % (ctime(), os.getpid()))
    multiprocessing.Process(target=demo).start()
    sleep(10000)
    print('[%s] %s father process end ... ...' % (ctime(), os.getpid()))

if __name__ == '__main__':
    main()
