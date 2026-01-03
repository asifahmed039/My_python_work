#Inheritence
"""
    When one class(child/Derive) derives the properties and methods of another class(parent/base).

            class Car:    #parent/base
                ......
            
                
            class ToyotaCar(Car):     #child/derive
                .........

"""
class car:
    color="green"
    @staticmethod
    def start():
        print("car start..")
    @staticmethod
    def stop():
        print("car stop..")


class toyota(car):
    def __init__(self,name):
        self.name=name

car1=toyota("fortuner")
car2=toyota("prius")
print(car1.start())
print(car2.color)
        

