#nesting if statement

#nesting
age=99
if(age>=18):
    if(age>=80):
        print("cannot derive")
    else:
        print("can derive")
else:
    print("can't derive")

#wap to check if a number entered by the user is odd or even

num=int(input("enter the number:"))
if(num%2==0):
    print("even num")
else:
    print("odd num")
#wap to find the greatest of 3 numbers entered by the user

num1=int(input("enter first number:"))
num2=int(input("enter first number:"))
num3=int(input("enter first number:"))

if(num1>num2 and num1>num3):
    print("Greatest no:",num1)
elif(num2>num3):
    print("Greatest no:",num2)
else:
    print("Greatest no:",num3)


#wap to check if a number is a multiple of 7 or not
num4=int(input("enter the number:"))
if(num4%7==0):
    print("number is multiple of 7")
else:
    print("not multiple of 7")
