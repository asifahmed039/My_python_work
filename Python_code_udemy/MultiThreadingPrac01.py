from threading import *
from time import *

def display():
    for i in range(3):
        print("System")

t=Thread(target=display)
t.start()
for i in range(5):
    print(i)

t.join()
