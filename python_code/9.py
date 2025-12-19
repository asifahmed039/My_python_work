name=input("enter your name :")
print(len(name))
print(name.count("a")) 

#Conditional statements
"""if-elif-else(syntax)
if(condition):
    statement1
elif(condition):
    statement2
else:
    statementn

"""

age=17
if(age>=21):
    print("can vote & apply for license")
    print("class")
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"): # proper spacing is called indentation  use in python instead of {}
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("no meaning")

print("end")

#wap grade student based on marks
marks=86
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"

print("grade of the student:",grade)
