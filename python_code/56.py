#Define a Circle class to create a circle with radius the constructor.
#define an Area() method of the class which calculates the area of the circle.
#define a perimeter() method of the class which allows you to calculate the parameter of the circle.


class Circle:
    def __init__(self,radius):
        self.radius=radius
    #area    
    def Area_cricle(self):
        return self.radius**2*(22/7)
    #perimeter
    def perimeter_circle(self):
        return self.radius*2*(22/7)
    
c1=Circle(21)
area=c1.Area_cricle()
print(area)
print(c1.perimeter_circle())