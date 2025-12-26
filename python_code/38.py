#





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