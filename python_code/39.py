"""
# class and Instance Attributes

    Class.attr
    obj.attr

    obj attr>>>class attr

"""





class student:
    college_name="ABC college"   #class attribute
    name="Anonymous"
    #parameterized constructors
    def __init__(self,fullname,marks):  # at the place of self we can also write anything ex  fffd, 
                                        #bgfh, but we use self for better readability.
        self.name=fullname    #object Attribute      #object attr >>> higher prec than class attr when 
        self.marks=marks      #object Attribute      #both have same name.
        print(self)
        print("adding new name in db.")

s1=student("ram",65)
s2=student("ram",65)
print(s1.college_name)
print(s2.college_name)
#access using class attribute with class name.
print(student.college_name)     #valid
print(s1.name,s1.marks)