#Super Method
""""
    Super() method is used to access methods of the parent class.

"""

class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car start..")

    @staticmethod
    def stop():
        print("car stop..")


class toyota(car):  #inherit class car
    def __init__(self,name,type):
            super().__init__(type)
            self.name=name
            super().start()

toyota1=toyota("inex","electic")
print(toyota1.type)
toyota1.type="democar"
print(toyota1.type)