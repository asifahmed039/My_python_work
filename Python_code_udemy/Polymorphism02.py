#Duck Typing
""""

"""

class Duck:
    def talk(self):
        print("duck talking")

    def walk(self):
        print("duck walking")

class Dog:
    def talk(self):
        print("dog talking")

    # def walk(self):
    #     print("dog walking")

def person(pet):
    pet.talk()
    if hasattr(pet,'walk'):
        pet.walk()

dog=Dog()
person(dog)
duck=Duck()
person(duck)

#second ex
class Tesla:
    def drive(self):
        print('Tesla Driving')

class Bugatti:
    def drive(self):
        print('Bugatti Driving')

def driver(car):
    car.drive()

car=Tesla()
driver(car)

