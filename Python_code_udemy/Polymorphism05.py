#Operator Overloading
""""
    Arithmetic operators
        Addition
        Subtraction
        Multiplication
        Division
        Floor division
        Modulue
        Exponents

        4+5  possible with addition operator
        1.5+6.2  possible with addition operator
        "Hi"+"Mr X"  Possible with addition called cancatination

        vector addition not possible with addition operation 
         v1+v2   
         so, Write class for vector addition
        
"""
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    
v1=Vector(3,1)
v2=Vector(2,5)
v3=v1+v2
print('vector sum:=',v3)
        