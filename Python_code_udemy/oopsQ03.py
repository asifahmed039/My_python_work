#Person Details
from datetime import date
class Person:
    def __init__(self,first_name,last_name,birth_year):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__birth_year=birth_year

    @property
    def name(self):
        return f'{self.__first_name} {self.__last_name}'
    @name.setter
    def name(self,name):
        names=name.strip().split()
        if len(names)!=2:
            raise ValueError("Full name must contains first and last name.")
        self.__first_name,self.__last_name=names
    @property
    def age(self):
        current_year=date.today().year
        return current_year-self.__birth_year
    
if __name__=="___main__":
    p=Person("John","Ahmed",1999)

    print("Asif")
