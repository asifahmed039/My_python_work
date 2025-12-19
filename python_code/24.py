#For loop
"""
Loop are used for sequential traversal. For traversing list,string,tuples etc.

for loops
[01]
for el in list:
    #some Work
[02]
for Loop with else
for el in list:
    #some work
else:
    work when loop ends

"""
nums=[1,2,3,4,5]
for val in nums:
    print(val)

#example
vegetables=["potato","brinjal","ladyfinger","cucumber"]
for el in vegetables:
    print(el,end=" ")
print("\n")    

#ex:--
str="Asif Ahmed"
for el in str:
    if(el=="m"):
        print("m found")
        break
    print(el,end=" ")
else:
    print("end")