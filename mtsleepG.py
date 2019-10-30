# mtsleepG.py

from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 20))) #  将列表生成式的[]改为（），就创建了一个generator。   randrange(3, 7)表示创建3~6个进程，randrange(2,5)表示为每一个进程选择一个睡眠时间
remaining = CleanOutputSet()

def loop(nsec):
    myname = current_thread().name
    with lock:
        remaining.add(myname)
        print('[%s] started %s' % (ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[%s] completed %s (%d secs)' % (ctime(), myname, nsec))
        print('  (remaining: %s)' % (remaining or 'None'))

def main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start() #  args=(pause, )中的','必不可少，如果没有，那么args就会被当做int

@register
def _atexit():
    print('all Done at:', ctime())

if __name__ == '__main__':
    main()

