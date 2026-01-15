#String Indexing
"""
    index 0,1,2,3,4........
    str='Hello World'
    str[0]    str[-7]  access allowed but 
    str[2]='M'   not allowed in string.
    because string is immutable.

    String Slicing:-
        s1[start:stop:step] same as
        range(1,10,2) 
    sequence data type:
    string,list,tuple



"""
str='Hello World'
str[6]
print(str[6])
#string sclicing start at 1 and end at 7th index.
print(str[1:7])
print(str[-5:])#always forward movement
print(str[-11:2])
print(str[0:11:2])#steping 2
#reverse the string using sclicing
print(str[::-1])
print(str[::-1])
print(str[8:2:-1])
