#Joining and Splitting
"""
    [01]replace(old,new,count)
    [02]join(stringNmae)
    [03]split(sep,maxsplit)
    [04]rsplit()  start from right side
    [05]splitlines(keepends)


"""
#replace()
s1='a-b-c-cd-e'
s2=s1.replace('-',"")
print(s2)
s2=s1.replace('-','',3)
print(s2)
s2=s1.replace('k','m')  #do nothing return same string.
s3="asifahmed@gmail.com"
s4=s3.replace("gmail",'outlook')
print(s4)

#join()
str='xyz'
str1='abc'
str3=str.join(str1)
print(str3)
str4='/'
str5='abc'
str6=str4.join(str5)
print(str6)

#split()
sr='jhon smith ajay'
sr2=sr.split() #return in list
print(sr2)
st3=sr.split('h')
print(st3)
sub='jhon,smith,ajay'
sub1=sub.split(',')
print(sub1)

f1='jhon-smith-ajay-khan-james'
f2=f1.split('-',3)
print(f2)

