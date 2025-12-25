#





class student:
    def __init__(self,fullname,marks):  #at the place of self we can also write anything ex  fffd, bgfh, but we use self for better readability.
        self.name=fullname
        self.marks=marks
        print(self)
        print("adding new name in db.")

s1=student("sunny",97)
print(s1.name,s1.marks)