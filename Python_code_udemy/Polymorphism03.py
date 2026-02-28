#Method overloading
""""
    same name function with different 
        [01]Types of parameters
        [02]Number of parameters
"""

def sum(a,b):
    return a+b

def sum(a,b,c=0):
    return a+b+c

print(sum(10,20))