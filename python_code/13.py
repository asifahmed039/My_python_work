#Tuples in python
"""
'A built-in data type that lets us create immutable sequences of values.'
            list  -----mutable
            tuple -----immutable
tup=(87,64,33,95,76)   "tup[0],tup[1]....."
tup[0]=43       "Not allowed in python"

tup=()   null tuple
tup=(1,)  single tuple always use comma after element rigth way to make single tuple tup=("hello",)
tup=(1,2,3,) optional 



"""

tup=(2,1,3,1)
print(tup[0])
print(tup[1])
# tup[0]=5  #give error
tup1=(1,)  #tup=(1)  type intger
print(tup1)
print(type(tup1))
print(tup[1:4])   #slicing allowed in tuple

#tuple methods
"""
tup=(2,1,3,1)

tup.index(el)  #returns indes of first occurrence  tup.index(1) is 1
02)tup.count(el) #counts total occurrences  tup.count(1) is 2"""

tup2=(1,2,3,4)
print(tup.count(2))
print(tup2.index(3))
