# coding: utf-8
# 测试多线程中join的功能
import threading, time


def doWaiting1():
    print('start waiting1: ' + time.strftime('%H:%M:%S') + "\n")
    time.sleep(3)
    print('stop waiting1: ' + time.strftime('%H:%M:%S') + "\n")


def doWaiting2():
    print('start waiting2: ' + time.strftime('%H:%M:%S') + "\n")
    time.sleep(6)
    print('stop waiting2: ', time.strftime('%H:%M:%S') + "\n")


if __name__ == '__main__':
    tsk = []

    thread1 = threading.Thread(target=doWaiting1)
    thread1.start()
    tsk.append(thread1)

    thread2 = threading.Thread(target=doWaiting2)
    thread2.start()

    tsk.append(thread2)

    print('start join: ' + time.strftime('%H:%M:%S') + "\n")
    for tt in tsk:
        tt.join()

    print('end main thread: ' + time.strftime('%H:%M:%S') + "\n")
