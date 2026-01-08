#Polymorphism
""""
    Polymorphism:-
        when the same operator is allowed to have different meaning according to the context.
            Operators and dunder function
            a+b #addition       a.__add__(b)
            a-b #subtraction    a.__sub__(b)
            a*b #multiplication a.__mul__(b)
            a/b #division       a.__truediv__(b)
            a%b #addition       a.__mod__(b)
        
"""
#'+' has different work with different data type. (operator overloding (implicit overloding))
print(1+2)#Sum
print(type(1))
print('asif'+'ahmed')#concatenate
print(type("Asif"))
print([1,2,3]+[4,5,6])#merge
print(type([1,2,3,4]))
x=1235469875626643223154633
y=1000000000000000000000000
print(x+y)


