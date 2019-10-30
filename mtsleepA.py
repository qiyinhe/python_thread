# mtsleepA.py

import _thread
from time import sleep, ctime

def loop0():
    print("Start loop 0 at:", ctime())
    sleep(4)
    print("Loop 0 done at:", ctime())

def loop1():
    print("Start loop 1 at:", ctime())
    sleep(2)
    print("Loop 1 done at:", ctime())

def main():
    print("Start at:", ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ()) #  第二个参数args是一个tuple，没有默认值，所以即使function没有参数，也要传入一个空tuple
    sleep(6)
    print("All done at:", ctime())

if __name__ == '__main__':
    main()


