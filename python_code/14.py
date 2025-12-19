#wap to ask the user to enter names of their 3 favorite movies & store them in a list.
           #first way to write code
movies=[]
mov1=input("enter first movie:")
mov2=input("enter 2nd movie:")
mov3=input("enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#second way to code

movies=[]
mov=input("enter 1st movie:")
movies.append(mov)

mov=input("enter 1st movie:")
movies.append(mov)

mov=input("enter 1st movie:")
movies.append(mov)

print(movies)

#third way to code
movies1=[]
movies1.append(input("enter the movies name:"))
movies1.append(input("enter the movies name:"))
movies1.append(input("enter the movies name:"))
print(movies1)