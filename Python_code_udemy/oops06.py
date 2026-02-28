#class Variable and Methods
"""
class variable is also used as share variable.
common to all objects

    class variable
        Declared outside all methods
        Create only once, common of all instance
        Can be accessed using object or class name
        Used as shared data
        Stores information about class(Meta Data)

    class methods
        Decorator @classmethod is used
        First parameter is cls class variable
        They can access only class variable

"""
class rectangle:
    count=0     #class variable or static variable
    def __init__(self,l=1,b=1):
        self.length=l
        self.breadth=b
        rectangle.count+=1       #class variable 

    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    @classmethod
    def get_count(cls):
        return cls.count
    
r1=rectangle(15,8)
r2=rectangle(7,4)
print(rectangle.count)
print(r1.count)
x=rectangle.get_count()
print(x)
