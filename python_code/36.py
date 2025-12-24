#from a file containing numbers separated by comma, print the count of even numbers.
#1,2,45,86,76
#1]individual----parse/casting to int
#first way
with open("practice1.txt","r") as f:
    data=f.read()
    print(data)
    num=""
    for el in range(len(data)):
        if(data[el]=="," or data[el]==" "):
            print(num)
            num=""
        else:
            num+=data[el]

#second way
with open("practice1.txt","r") as f:
    data=f.read()
    print(data)
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            print("even",val)
        else:
            print("odd no",val)


