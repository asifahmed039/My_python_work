"""name=input("name: ")
print(name)
print("yes")if 4==5 else print("no")
a=9
print(type(a))
print("sweet") if a>=10 else print(a)
a=str(a)
print(type(a))
sal=float(input("enter salary "))
tax=sal*(0.1,0.2)[sal>50000]
print(tax)"""
# import os  #pre install 
# str="thanks for coming."
# print(str.endswith("."))


# with open("go.txt","r") as f:
#     print(f.read())

# # file=open("first.txt","r")
# # print(file.read())

# #os function
# os.remove("first.txt")
# set={1,2,3,4,5,5,6,6}
# print(len(set))
# set.pop()
# print(set)
# set.add(200)
# print(set)

class student:
    college_name="gobal institute of engineering and technology"
    def __init__(self):
        pass
    def gets_marks(self):
        print("marks:",self.mark)

    def input_marks(self,marks):
        self.mark=marks


s1=student()
s1.input_marks(95)
print(s1.gets_marks())