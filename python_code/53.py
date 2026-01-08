#Properties
"""
Property:
    We use @property decorator on any method in the class to use the method as a property.
     atuomatic change occur when any change in object atrr.


     search to learn
        @getter
        @setter
     
"""

class student:
    def __init__(self,phy,chm,math):
        self.phy=phy
        self.chm=chm
        self.math=math
        # self.percentage=str((self.phy+self.chm+self.math)/3)+"%"

# def cal_percentage(self):
#     self.percentage=str((self.phy+self.chm+self.math)/3)+"%"

    @property
    def cal_percentage(self):
        return str((self.phy+self.chm+self.math)/3)+"%"

s1=student(98,97,96)
# print(s1.percentage)
s1.chm=86
print(s1.chm)
print(s1.cal_percentage)



    