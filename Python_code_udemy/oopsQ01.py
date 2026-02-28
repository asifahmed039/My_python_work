#Cricle class
""""
    Area=pi*r*r
    pi=3.14159
    peremeter
    maths modulue contains:
        float function              Trigonometry Function        power & log function
            math.floor(5.6)             sin(x)  cos(x)              pow(x,y) sqrt(x)
            math.cell(5.6)              tan(x)  degree(x)           cbrt(x)  
            math.trunc(5.6)
            math.fabs(x)

"""
import math
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2 * math.pi
    def perimeter(self):
        return 2*self.radius*math.pi
radius=int(input("Enter the radius of circle:"))
c1=Circle(radius)
x=c1.area()
print(f'Area:{x:.2f}')
