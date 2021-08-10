import time
import threading


# 新线程
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("")


time.sleep(1)
