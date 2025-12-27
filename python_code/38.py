#__init__ function
#constructor in python
"""
   constructor:---
        All classes have a function called __init__, which is always executed when the object is 
        being initiated.

        #creating class                                            #creating object
            class student:                                             s1=student("karan")
                def __init__(self,full_nmae):                          print(s1.name)
                    self.name=fullname

    Self:--
        The self parameter is a reference to the current instance of the class and is used to access 
        variables that belongs to the class.
            
"""

class student:
    #default constructors
    def __init__(self,fullname,marks): 
        pass

    #parameterized constructors
    def __init__(self,fullname,marks):  # at the place of self we can also write anything ex  fffd, 
                                        #bgfh, but we use self for better readability.
        self.name=fullname
        self.marks=marks
        print(self)
        print("adding new name in db.")

s1=student()
print(s1.name,s1.marks)