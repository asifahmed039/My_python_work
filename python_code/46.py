#Private(like) attribute and methods
""" 
    #Conceptual implementation in Python
        Private attributes & methods are meant to be used only within the class and
        are not accessible from outside the class.

                    Public        private


    
"""

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass   #private attribute __(double underscore)

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account(12345,"abcedf")
print(acc1.__acc_pass)   #give error private attr can't access from outside the class.
print(acc1.reset_pass())  #allow --------

#private methods
class Person:
    __name="anonymous"    #private attribute
    def __hello(self):   #private function
        print("hello person!..")
    def welcome(self):   #public
        self.__hello()
p1=Person()
print(p1.welcome())

