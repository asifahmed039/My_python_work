#Static Methods
"""
    Methods that don't use the self parameter(work at class level)
        class student:
            @staticmethod    #decorator
            def college():
                print("abc college)
        
    Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
    without permanently modifying it.

"""
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod               #decorator    
    def hello_print():
        print("welcome...")

    def avg_marks(self):
        sum=0
        for el in self.marks:
            sum+=el
        print("hi,",self.name,"avg of marks:",sum/3)

        
s1=student("sunny",[91,65,49])
s1.name="tonneyShark"
print(s1.avg_marks())


