#Lists in python
"""A built-in- data type that stores set of values 
It can store elements of different types (integer,float,string,etc...)

             access allowed in   but change not allowed strings----immutable
             access and change both are allowed in lists------mutable

marks=[87,64,33,95,76]        #marks[0],marks[1].....
student=["Karan",85,"Delhi"]  #student[0],#student[1].....
student[0]="Arjun" #allowed in python
#####    len(student)   #returns length

"""

student=["Karan",95.4,17,"Delhi"]
print(student)
student[3]="hyderabad"
print(student)
# print(student[5])       #its give error range 
 
 # List Slicing 
"""
Similar to string slicing
list_name[string_idx:ending_idx] #ending index not included

marks=[87,64,33,95,76]
marks[1:4] is [64,33,95]
marks[:4] is same as marks[0:4]
marks[1:] is same as marks[1:len(marks)]
marks[-3:-1 is [33,95]]

"""
marks=[87,64,33,95,76]
print(marks[1:])
print(len(marks))

