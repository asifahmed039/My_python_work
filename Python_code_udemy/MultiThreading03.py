#Mutex and semaphore
"""
    when thread try to access same resource then
    lock() use to control the access


"""
from threading import *
from time import *

def display(strl):
    l.acquire()
    for x in strl:
        print(x)
        sleep(1)
    l.release()

l=Lock()
t1=Thread(target=display,args=('Hello World'))
t2=Thread(target=display,args=('you are welcome',))

t1.start()
t2.start()

t1.join()
t2.join()




