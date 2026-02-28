#[228]Polymorphism
""""
    poly means many  morphism  means form
        [one name many form]

    
"""
a=4+5  #integer
print(a)
a=1.7+3.6  #float
print(a)
a='Hello'+'world'  #string
print(a)
"""
operator overloading:-
    one operator + but different work perform with different data type.

"""
l=[1,2,3,4,5]
a=len(l)
print(a)

l={1,2,3,4,5}
a=len(l)
print(a)

l='hello'
a=len(l)
print(a)

"""
    Methods Overloading:-
        len() perform different operation with different data type.

"""
def sum(seq):
    s=0
    for i in seq:
        s+=i
    return s

print(sum([10,10,10,20]))


