#Constructor and self
"""
  self 
    id(object_name)    reference for current object.
    
"""

class rectangle:
    def __init__(self,l=1,b=1):
        print('self id',id(self))
        self.length=l
        self.breadth=b

    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
r1=rectangle(15,8)
r2=rectangle(7,4)
r3=rectangle()   # its take default argument
print('r1 id',id(r1))

