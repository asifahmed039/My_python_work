#project 
"""
Guess the correct number.
"""
import random as ran

target=ran.randint(1,100)
# print(randNum)

while True:
    userChoice=input("Guess the target number or type 'Quit' for end the race:")
    if(userChoice=="Quit"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success: Correct Guess!!")
        break
    elif(userChoice<target):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")



print("-------Game Over----------------")