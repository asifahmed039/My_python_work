#Method overriding
"""
    two or more methods have same name in program
    ex:- given below
    polymorphism achieved

"""
class Parent:
    def show(self):  #overriding
        print('Parent Class')

class child(Parent):
    def show(self):   #overRiding
        super().show()
        print('child Class')

c=child()
c.show()
c.super().show()    #its give error can't access outside with super()
