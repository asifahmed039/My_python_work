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
g='z' not in s6 #give true if not present in s6.
print(g)

"""
    string comparision
        Dictionary order , Lexicography order
        ex:--
            apply>apple  , cat<catch , data>Data, 2nd<Byte 

            0<1<2<3......<A<B<C.....a<b<c<...... Due to Ascii 
            (48-57)      (65-90)    (97-122)  

"""
s1='software'
s2='haedware'
print(s1==s2)
print(s1>s2)
for i in s1:
    print(i)
list=[10,5,2,30]
for i in list:
    print(i)
list[0]=50
print(list[0])