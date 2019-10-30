# mtsleepC.py

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print("Start loop %d at:" % nloop, ctime())
    sleep(nsec)
    print("Loop %d done at:" % nloop, ctime())

def main():
    print("Start at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)


    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at:", ctime())

if __name__ == '__main__':
    main()
