#[78]Prefix and Suffix of a string
"""
    [01]startswith(prefix,start,end)
    [02]endswith(suffix,start,end)
    [03]removeprefix(prefix)
    [04]removesuffix(suffix)
    [05]partition(sep)
    [06]rpartition(sep)

    ex:-
    s1=Rossum@gmail.com
"""

str='python is very easy'
#starwith()
res=str.startswith('python')
print(res)
res1=str.startswith('is')
print(res1)
print(str.startswith('is',7))
#endwith()
print(str.endswith('easy'))
s1='Rossum@gmail.com'
print(s1.endswith('.com'))
print(s1.endswith('java'))
#removesuffix()
s2=s1.removeprefix('Ross')
print(s2)
#partition()
s4=s1.partition('.')
print(s4)
#rpartition()
s5=s1.rpartition('s') #from right hand side.
print(s5)



