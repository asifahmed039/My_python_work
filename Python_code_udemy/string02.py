#string operator
"""
    [01]Concatination  +
    [02]Repetition  *
    [03]Membership in,not in
    [04]String comparision <,>,<=,>=,==,!=
"""

s1='wel'
s2='come'
s3=s1+s2  #concatination
print(s3)

s4='x'
s5=s4*10  #repetition
print(s5)

s6='abcdef'
d='a' in s6  #true if present in s6.
print(d)
g='z' not in s6
print(g)