#instance Variable and Methods
"""
Object are also called intance of class

    Variable Type 
        Instance:-Variable which is present in object(instance) is called instance variable.
            its declare with self always and within __init__().
            self. instance variable accessed using self.
            self is not keyword.

        Class
        Static

    Methods
        Instance:-Methods which present in instance is known as Instance Method.
            its take self as parameter always.
        Class
        Static
    

"""
class rectangle:
    def __init__(self,l=1,b=1):
        print('self id',id(self))
        self.length=l   #instance variable
        self.breadth=b   #instance variable

    def area(self):
        return self.length*self.breadth    #instance methods
    
    def perimeter(self):
        return 2*(self.length+self.breadth)    #instance methods
    
r1=rectangle(15,8)
r2=rectangle(7,4)
r3=rectangle()   # its take default argument

class test:
    def __init__(self):
        self.a=10         #instance variable
    def fun(self):
        self.b=20
    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)

t=test()
t.fun()
t.c=90
t.show()


