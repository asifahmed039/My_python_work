#Inheritance types
"""
    Types
    [01]Single inheritence    []----[]
    [02]Multi-level inheritance   []-----[]----[]-----[]---
    [03]Multiple inheritence

     
"""
#Single Inheritence

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