#lets practice
"""
waf to print the length of a list.(list in parameter)
"""
list=[10,30,20,40,45,55 ]
def lenght_list(x):
    print(len(x))
lenght_list(list)
cities=["delhi","gurgaon","noida","pune","hyderabad"]
lenght_list(cities)


#waf to print the element of a list in a single line.(list is the parameter)
def print_list(x):
    for el in x:
        print(el,end=" ")

print_list(cities)
print()

#waf to find the factorial of n.(n is the parameter)
#recursion used
def fact(n):
    if(n==0 or n==1):    
        return 1
    return n*fact(n-1)
print(fact(5))

def fa(n):
    fact=1
    for el in range(1,n+1,1):
        fact*=el
    return fact
print(fa(5))

#waf to convert usd to inr.

def conerter(usd_vl):
    inr_vl=usd_vl*90
    print(usd_vl,"usd=",inr_vl,"inr")
conerter(10)
    


    