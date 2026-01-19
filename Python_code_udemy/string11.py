#[80]Inquiry Methods
"""
inquiry methods 
    boolean result (t/f)

    [01]isalpha()
    [02]islower()
    [03]isupper()
    [04]istitle()
"""
s='Hello'
x=s.isalpha()
print(x)

x=s.islower()
print(x)

x=s.isupper()
print(x)

str='Hello World'
x=str.istitle()
print(x)

"""
    isspace()   
        ' ' , '    ' ,\n\v\r\f  control characters (colsor)  white space, '' empty space

    isprintable()
        all unicodes except escape sequences  \n\v\r\b\a esc

    isidentifier()
        variable name is identifier 
        isidentifier use to check the identifier is valid or not.
            item1   valid
            1item   invalid


"""
s='      '
print(len(s))
print(s.isspace())

s=""
print(len(s))
print(s.isspace())








