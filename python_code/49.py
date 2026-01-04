#Multiple inheritence

class car:
    
    @staticmethod
    def start():
        print("car start..")
    @staticmethod
    def stop():
        print("car stop..")


class toyota(car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(toyota):
    def __init__(self,type):
        self.type=type

Fortuner1=Fortuner("Petrol")
Fortuner.start()

