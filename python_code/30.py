#two types of function in python
"""
[01]Built in functions 
    print(),len(),type(),range()

[02]User defined functions

"""

print("hello...")  #built in fun  here hello is argument
print("hello..","world") # sep=" "
print("hello...")#end="\n"
print("world")
print("mira",end="@")
print("bigha")
# range()

"""
    Default Parameters
        Assigning a default value to parameter, which is used when no argument is passed.
"""
#user define function
def product(a=1,b=1):  #(a=1,b) throw error because default value start from left side (a,b=1),(a=4,b=2),(a,b=1,c=5)
    return a*b
print(product())


