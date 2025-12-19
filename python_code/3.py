#practice code
'''x,y,z=100,20,30
print(x,y,z)
div=x//20
print(div,x/y,25/3)
name=input("enter your namea :")
print(name)
num=int(input("enter the number"))
print(num)'''
#time 1:22 to 1:44
#Conditional statements
'''
if-elif-else(syntax)
if(condition):
    statement1
elif(condition):
    statement2
else:
    statemet3  '''
 

light=input("Light colour :")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("ready")
else:
    print("danger")

#Grade of students
marks=int(input("enter your marks :"))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("c")
else:
    print("D")

#single line if /Ternary operator
'''<var>=<var>if<condition>else<var2>'''
food=input("food: ")
eat="yes"if food=="cake" else "no"
print(eat)

'''<statement> if <condition> else <stt2>'''

food=input("food :")
print("sweet") if food=="cake" or food=="jalebi" else print("no sweet")

