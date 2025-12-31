#create student class that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print the average.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg_marks(self):
        sum=0
        for el in self.marks:
            sum+=el
        print("hi,",self.name,"avg of marks:",sum/3)

        
s1=student("sunny",[91,65,49])
s1.name="tonneyShark"
print(s1.avg_marks())
