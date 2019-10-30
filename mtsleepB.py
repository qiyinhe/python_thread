# mtsleepB.py

import _thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print("Start loop %d at:" % nloop, ctime())
    sleep(nsec)
    print("Loop %d done at:" % nloop, ctime())
    lock.release()

def main():
    print("Start at:", ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))


    for i in nloops:
        while locks[i].locked():
            pass
    print("All done at:", ctime())

if __name__ == '__main__':
    main()
