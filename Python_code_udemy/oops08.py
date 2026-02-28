#Property Methods
"""
class rectangle
    def __init__(self,l,b):
        set.lenght(l)
        self.breadth=b


r1=rectangle()
r1.length=-10
    but length can not be negative 

we use methods

def set_length(self,l):
    if 1>=0:
        self.lenght=l
    else:
        self.length=1

def get_length():
    return self.length

    but issue is we can't access with r1.lenth=10 and its give error
    so use property decorator

"""
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    @property    
    def length(self):
        return self._length
    @length.setter
    def length(self,l):
        if l>=0:
            self._length=l    #underScore is important otherwise give error
        else:
            self._length=1

r1=Rectangle(10,10)
x=r1.length
print(x)

