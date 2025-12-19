# i=1
# n=int(input("enter number:"))
# while i<=10:
#     print(n*i)
#     i+=1

# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[i])
#     idx+=1

# i=1
# while(i<=10):
#     if(i%2!=0):
#         print(i)
#     i+=1

# n=3
# for i in range(1,11):
#     # print(i*n)
#     pass
# print(n)

# sum=0
# n=int(input("enter numbar:"))
# # for i in range(1,n+1):
# #     sum+=i
# # print(sum)
# i=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

# def cal_sum(a,b):
#     sum=a+b
#     return sum

# add=cal_sum(10,20)
# print(add)



# def hello_fun():
#     print("hello....",i)
# for i in range(1,10):
#     hello_fun()

f=open("name.txt","a+")
# dataw=f.read()
# data=f.readline()
# data1=f.readline()
# print(dataw)
# print(data)
# print(data1)

# print(f.read())
# f.write("Hello India ")
# f.write("\ni love my country.")
# data=f.read()
# print(data)
# f.close()

#class and objiect
# class student:
#     name="sunny"

# s1=student()
# print(s1.name)

with open("C:\Users\asifa\OneDrive\Desktop\New folder\name.txt","r") in f:
    content=f.readline()
    print(content)