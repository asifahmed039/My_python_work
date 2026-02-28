#Static Methods
"""
when we write this
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def cal_area(lenght,breadth)
        return length*breadth
    
r1=rectangle(15,8)
print(r1.cal_area(10,8))

give error you pass less parameter 
because first parameter treat as self (reference)
its work 
when call with class name
recangle.cal_area(10,8)



        

"""
""""
    static methods
        Utility functions
        Can be called using class name
        can't access members of a class
        
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
    
    
r1=rectangle(15,8)
r2=rectangle(7,4)
 