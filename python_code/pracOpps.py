class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    @staticmethod
    def welcome():
        print('Welcome  to my Village......')
    
    def get_details(self):
        print(f"name: {self.name} and rollno: {self.rollno}")
    
s1=student('Rohan',504)
s1.welcome()
s1.get_details()
s2=student('Sohan',505)
s2.welcome()
s2.get_details()
    
        


        