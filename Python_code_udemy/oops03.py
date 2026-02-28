#How to  write a class
"""
 __init__   intialization
    self     referance (current object)

"""
class rectangle:
    def __init__(self):
        self.length=10
        self.breadth=5
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
r=rectangle()
print(f'length {r.length}')
print(f'breadth {r.breadth}')
print(f'Area {r.area()}')
print(f'peremter {r.perimeter()}')


