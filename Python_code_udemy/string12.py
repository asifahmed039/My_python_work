#More inquiry methods
"""
    (01)isdigit()
            {'7235' digit}   {'71.23' not digit}

    (02)isdecimal()
    (03)isnumeric()
    (04)isascii()
    (05)isalnum()

    """

s='783.87'
print(s.isdigit())

#subscript search on website unicode
s='7\u20823\u2075'
print(s,s.isdigit())



#isdecimal()   used for any language hindi or english
print(s.isdecimal())
s1='2345'
print(s1.isdecimal())
s='\u0969\u096A\u096B'
print(s.isdecimal(),s)

s2='-3.75ab'
print(s2.isdecimal())

