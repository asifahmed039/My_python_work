#Alignment and padding
""""
Just methods 
    are use to add spaces in string.

    01)ljust(width,fillChar)

    hello1******* left align
    02)rjust(width,fillChar)

    ********hello  right align

    03)zfill(width)

"""
s="hello"
#ljust()
x=s.ljust(7,'*')
print(x) # hello**
#rjust()
x=s.rjust(7,'*') #**hello
print(x)
#center()
x=s.center(7,'#')
print(x)
#zfill()
x=s.zfill(7)
print(x)  #with leading 0

#Strip() methods
"""
    Strip mehtods
        are use to remove spaces from string.

        01)lstrip(chars)
        02)rStrip(chaes)
        03)strip(char)

        important for machine learning and data science.

"""
s="  Hello"
print(s)
x=s.lstrip()  #remove space from left side.
#lstrip()
print(x)
s="@@Hello"
print(s.lstrip('@'))
#rstrip()
s="Hello!!"
print(s.rstrip('!'))
#strip()
s='^hello^'
print(s.strip('^'))
"""
        #!hello  $ * how remove 

"""
s='#!hellos  $ *'
print(s.strip('#! $*'))
