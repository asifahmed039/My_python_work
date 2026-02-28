#Inheritance
"""
    borrow things from other class is called Inheritance.
    Inheritance provide to achieve reusibility.
    Ex:-
        Rectangle  Cuboid class

"""
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def Area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*self.length*self.breadth
class Cuboid(Rectangle):
    def __init__(self,h):
        self.height=h
    def volume(self):
        return self.length*self.breadth*self.height
    """
        some thing is missing here 
        Discuss in next file.
        here when object are created they only call child __init__ function(construction)
        not parent __init function
        so use super().__init(parameter)
    """
        