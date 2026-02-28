#Data Hiding
"""
    Pubilc: 
    Private __(dunder)

"""
class Parent:
    def __init__(self,d):
        # self.data=d  #public
        self.__data=d  #private  __ dunder

    def show(self):
        print(self.__data)
class Child(Parent):
    def __init__(self, d):
        super().__init__(d)
    
    def display(self):
        print(self.__data)

p=Parent(10)
p.show()
# p.__data=20  #but not change the value because its private
p._Parent__data=20
p.show()
c=Child(30)
c.show()
c.display() #its give error not access outside the class methods
