#class String
s1='hello'   #any thing which we write in double or single quotes is object.
print(type(s1))
"""
class and object
        example:-- house and its blueprint(design)
    class str contains 
        data (string,length)
        and methods find(),index(),endswith(),lower().upper()


"""
"""
    find(sub.start,end)
    rfind(sub.start,end)
    index(sub.start,end)
    rindex(sub.start,end)
    count(sub.start,end)
"""
print(s1.capitalize())
print(s1)
# print(dir(str))
#find('value',start,end)
print(s1.find('l',3))  #if not present then give -1.
print(s1.rfind('h'))
print(s1.index('l'))  # substring is not there it's give error
print(s1.count('l'))