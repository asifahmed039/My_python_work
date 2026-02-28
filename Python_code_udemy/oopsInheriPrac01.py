class college:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class depart(college):
    def __init__(self,departname,name,rollno):
        self.depart_name=departname
        super().__init__(name,rollno)

    def get_details(self):
        print(self.name," ",self.rollno," ",self.depart_name)

s=depart("civil","Ariz Ahmed","2025")
s.get_details()
        