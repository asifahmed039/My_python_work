#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)

#search for a number x in this tuple using:
#[1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
x=64
idx=0
for el in list:
    if(el==x):
        print("found", idx)
        break
    idx+=1
