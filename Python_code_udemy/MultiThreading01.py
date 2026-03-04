#Multithreding
""""
    Read theory part from chatgpt and use some other platfroms.

    Process:-Running program is process.

    MultiTasking:-Two different process are runnung simultaneously

    Multithreading:-Single program have multiple prcess flow of control
    ex:-Animation, Game car race etc...

    Ways of Multithreading :--

"""
from threading import *
from time import *

def display():
    for i in range(65,91):
        print(chr(i))
        sleep(1)

t=Thread(target=display,name='Alphabets')
t.start()
for i in range(65,91):
    print(i)
    sleep(1)
t.join()

