#Important Concept of oops
"""
    Abstraction:---
        Hiding the implementation details of a class and only showing the essential features to the user.

    Ecapsulation:---
        Wrapping data and functions into a singile unit(object).
    
    

"""

class car:
    def __init__(self):   #constructor
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True   #abstract it from user (hide)
        self.acc=True      #abstract it from user (hide)
        print("car started...")  #show to user

car1=car()
car1.start()