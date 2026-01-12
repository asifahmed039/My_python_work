"""
    Define a employee class with attributes role,department and salary.This class also showDetails() method.
    create an engineer class that inherits properties from employee and has additional attribute:name and age.
"""
class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    
    def show_details(self):
        print("role:",self.role)
        print("department:",self.department)
        print("salart:",self.salary)
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it",120000)

e1=employee("accountant","finance",55000)
e1.show_details()
e2=engineer("sunny",26)
e2.show_details()
