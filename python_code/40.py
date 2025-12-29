#methods in python
"""
    Methods are functions that belong to objects.

"""
class student:
    college_name="ABC college"   #class attribute
    
    
    def __init__(self,fullname,marks):    
                                        
        self.name=fullname    
        self.marks=marks      #object Attribute
        print(self)
        # print("adding new name in db.")
    #methods
    def welcome(self):
        print("welcome to college",self.name)
    def get_marks(self):
        return self.marks


s1=student("ram",65)
s1.welcome()
print(s1.get_marks())