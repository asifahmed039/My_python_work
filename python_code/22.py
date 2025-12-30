#print numbers from 100 to 1.
i=100
while i>=1 :
    print(i,end=" ")
    if(i%10==1):
        print("\n")
    i-=1
#print the multipication table of  a number n.
num=int(input("enter the number:"))
i=1
while i<=10 :
    print(num*i,end=" ")
    i+=1
#print the elements of the following list using a loop:
#[1,4,9,25,36,49,64,81,100]
list=[1,4,9,25,36,49,64,81,100]
i=0
while i<=len(list)-1 :
    print(list[i]) 
    i+=1
#search for a number x in this tuple using loop.
#(1,4,9,16,25,36,49,64,81,100)
i=0
lis=(1,4,9,16,25,36,49,64,81,100)
x=100
while i<len(lis) :
    if(lis[i]==x):  #******x==list[i]  
        print(i)
    i+=1
if(i==len(list)):
    print("not found")
