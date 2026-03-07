from threading import *
from time import *

class Number(Thread):
    def display(self):
        for i in range(5):
            print("hello")

n=Number()
n.start()
for i in range(6):
    print("mr.bean")
    sleep(1.5)
n.join()
