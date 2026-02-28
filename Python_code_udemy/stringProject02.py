#[83]Palindrome string
"""
    palidrome word:
        Madam   madaM
        Malayalam  
    
    palidrome Phrase:
        Name now one man   namenoonemaN
        Never odd or even
        Was it a car or a cat i saw
    
    Making a palindrome
     orginal string + reverse string
     


"""
str='Race Car'
strl=str.replace(' ','')
str_rev=strl[::-1]
if strl.casefold()==str_rev.casefold():
    print(str)
else:
    palindrome=str.casefold()+str_rev.casefold()
    print(palindrome)