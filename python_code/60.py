#Random Password Generator
#Project 02

import random
import string

# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.digits)
# print(random.choice("hello"))

pass_len=12 #take according to your need
charValues=string.ascii_letters+string.digits+string.punctuation

#first way to do 
#using list comprehension
res="".join([random.choice(charValues) for el in range(pass_len)])
#.join are use to cancatinate the character
print(res)



#second way to do
# passward=''
# for el in range(pass_len):
#     passward+=random.choice(charValues)
# print("your random password is:",passward)
