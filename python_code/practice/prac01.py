#Write a program to input 2 number & print sum
# str=input("enter the name \n")
# print(str.capitalize())

# num=str.count("s")
# print(num)
# print(str.find("i"))

# my_list=[1,2,2,3,44,44,5,4,]
# element=set(my_list)
# print(type(element))
# element=list(element)
# print(element)  

# def rupee_converter(a):
#     inr=a*90
#     print(a,"usd=",inr,)

# rupee_converter(1)
# # rupee_converter()

# #recursion in python
# def show(n):
#     if(n==0):    #termination condition
#         return
#     show(n-1)
#     print(n)

# show(10)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# def sum_0f_n(n):
#     if(n==0):
#         return 0
#     return n+sum_0f_n(n-1)
# sum=sum_0f_n(5)
# print(sum)

f=open('class.txt', 'r')
data=f.read()
print(data)
f.close()

print("hello")


