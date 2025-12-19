#let's practice
#wap to find the sum of first n numbers.(using while)
num=int(input("enter the number:"))
print(int((num*(num+1))/2))

i=1
n=5
sum=0
#while loop
while i<=n:
    sum+=i
    i+=1
print(sum)

#range
sum=0
num=int(input("enter the number:"))
for i in range(1,num+1,1):
    sum+=i
print(sum)

#wap to find the factorial of first n numbers.(using for)
fact=1
for i in range(1,n+1,1):
    fact*=i
print(fact)
