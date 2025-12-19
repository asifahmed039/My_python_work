#wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary & 
#add one by one. Use subjects name as key & marks as value.
marks={}
x=int(input("enter phy:"))
marks.update({"phy":x})

x=int(input("enter math:"))
marks.update({"math":x})

x=int(input("enter chem:"))
marks.update({"chem":x})
print(marks)

#figure out a way to store 9 and 9.0 as seperate values in the set.
#(you can take help of built in data types)

set={("int",9),("float",9.0)}
print(set)