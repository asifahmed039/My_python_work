#Semaphore
"""
    use chatgpt to read theory part
"""
from threading import *
from time import *

def display(strl):
    l.acquire()
    for x in strl:
        print(x,end='')
        sleep(1)
    print('\n')
    l.release()

l=Semaphore(1) # 1 means allow once at a time
t1=Thread(target=display,args=('Hello World',)) #tuple always single item must use
t2=Thread(target=display,args=('you are welcome',))
t3=Thread(target=display,args=('7250292681',))

t3.start()
t1.start()
t2.start()
t3.join()
t1.join()
t2.join()