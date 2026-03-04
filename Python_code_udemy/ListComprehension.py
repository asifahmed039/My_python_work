#List Comprehension
""" 
    List comprehension is short and clean way to create a list in python.

"""

a=[1,2,3,6,4,8,9]
even_no=[n for n in a if n%2==0]
print(even_no)
details=["even" if n%2==0 else "odd" for n in a]
print(details)