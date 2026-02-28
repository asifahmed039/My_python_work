#Construction in Inheritance
"""

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
    def __init__(self,l,b,h):
        self.height=h
        super().__init__(l,b)   #solution 
    def volume(self):
        return self.length*self.breadth*self.height
    
c=Cuboid(10,10,10)
print(c.volume())