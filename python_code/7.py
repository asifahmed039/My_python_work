#chapter 02 strings & conditional statements
#Strings
"""String is data type that stores a sequence of characters.
Basic operation
[1]Concatenation "hello"+"world"------>"helloworld"
[2]Length of stlr  len(str)

"""
#three different way to represent string in python
str="this is string."
str2='Apnagroup'
str3="""this is a string2."""
# why we use three way to represent string in python.
# 'this is mychannel's videos' how compiler uderstand the end 
str4="welcome to\n hyderabad" 
print(str4)
str5="Asif"
str6="Ahmed"
final_name=str5+" "+str6   #cancatenation
print(final_name)

#escape sequence character  \n,\t 
print(len(final_name))
print(str5[0])
#indexing 
""" "apna_college
     01234567891011
     str[0] is 'a" access allow
     str[0]='b'  not allow in python (give error)
     """
#slicing #******
#Accessing parts  of a string 
#important for machine learning
#str[staring_idx:ending_idx] #ending idx is not include
str="ApnaCollege"
str[1:4]
print(str[5:8])
print(str[5:])
print(str[4:len(str)])#*****

#slicing with negative index
""" A P P L E
    -5-4-3-2-1"""
str="APPLE"
print(str[-5:-1])  #******


