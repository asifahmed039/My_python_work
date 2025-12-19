#Loops in python

#[01] While loop
""""
Loops are used to repeat instructions.
 
    while loops 
    SYNTAX:---
       while condition:
            #SOME WORK

"""

# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

#use loops concept here
i=0
while i<=5 :
    print("hello")
    i+=1
print("count=",i)

#print numbers from 1 to 5
i=5
while i>=1:
    print(i)
    i-=1
#print numbers from 1 to 100.
i=1
while i<=100 :
    print(i,end=" ")
    if(i%10==0):
        print("\n")
    i+=1
