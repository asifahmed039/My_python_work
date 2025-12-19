#clever if| ternary operator

'''<var>=(flase_val,true_val)[condition]'''
age=int (input("age :"))
vote=("yes","no")[age>=18]
print(vote)
sal=float(input("salary :"))
tax=sal*(0.1,0.2)[sal<=50000]
print(tax)
#Calculate Simple interest
principle_amount=float(input("enter the amount :"))
rate_of_interest=float(input("rate of interest :"))
time=float(input("time :"))
simple_interest=(principle_amount*rate_of_interest*time)/100
print(simple_interest)
#Operators and its type

"""

An operator is a symbol that performs a certain operands.
1 Arithmetic operators (+,-,*,/,%)
2 Relational/Comparison operators (==,!=,>,<,>=,<=)
3 Assigment Operators (=,+=,-=,*=,/=,%=,**=)
4 Logical Operators (not,and,or)
"""
#Arithmetic operator
a=2
b=2
print(a+b,"\t",a-b,"\t",a*b,"\t",a/b,"\t",a%b)
print(a**b)#power 
