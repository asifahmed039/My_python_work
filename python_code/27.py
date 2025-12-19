#print numbers from 1 to 100.
for i in range(1,101,1):
    print(i,end=" ")

#print numbers from 100 to 1.
for i in range(100,0,-1):
    print(i,end=" ")

#print the multiplication table of a number n.
n=int(input("enter the number:"))
for i in range(1,n+1,1):
    print(n*i)

#pass statement

"""
 pass statement:
    pass is a null statement that does nothing. it is used as a placeholder for furture code.

    for el in range(10):
     pass
     

     for i in range(5):   #give error
    #empty
    print("name Asif Ahmed")

     
"""

for i in range(5):
    pass
print("name Asif Ahmed")

