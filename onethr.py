# onethy.py

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
    loop0()
    loop1()
    print("All done at:", ctime())

if __name__ == '__main__':
    main()


