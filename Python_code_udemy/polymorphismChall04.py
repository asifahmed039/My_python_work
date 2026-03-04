#student details
"""
    Serialization 
        import pickle
    Pickling:
        pickl.dump(student,file)
    unpickling:
        student=pickle.load(file)


"""
import pickle
class Student:
    def __init__(self,stud_id,name,marks):
        self.stud_id=stud_id
        self.name=name
        self.marks=marks

    def __repr__(self):
        return f"{self.name} ({self.stud_id})-Marks:{self.marks}"
    
def save_students(student_list,filename='students.pkl'):
    with open(filename,'wb') as f:
        pickle.dump(student_list,f)

def load_students(filename='student.pkl'):
    with open(filename,'rb') as f:
        data=pickle.load(f)
        return data

if __name__=="__main__":
    students=[
        Student('S001','Neil',{"Maths":75,"Science":80}),
        Student('S002','Ram',{"Maths":85,"Science":90}),
        Student('S003','Mohan',{"Maths":65,"Science":95})
    ]

save_students(students)
load_students=load_students()

print('Student Records:')
for i in load_students:
    print(i)
    
        