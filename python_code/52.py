#class Method
"""
     A class method is bound to the class and receives the class as an implicit first arguments.

     note:--
          static method can't access or modify class state & generally for utility.

          @classmethod

          class student:
              @classmethod  #decorator
              def college(cls):
                  pass
                  
        methos in python are:--
        [1]Static Method
        [2]Class Method
        [3]Instance Method

    
"""
class Person:
    name='anonymous'
    # def changeName(self,name):
    #     # self.name=name
    #     #Person.name=name    #access the class attr (01)
    #     self.__class__.name=name     #access the atrr of class (02)
    @classmethod
    def changeName(cls,name):   #(03)
        cls.name=name



p1=Person()
p1.changeName('sunny')
print(Person.name)
print(p1.name)