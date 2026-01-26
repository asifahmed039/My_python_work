#[84]Anagrams
"""
   decimal   medical
   state     taste
   listen    silent

   snooze alarms   alas, no more z's

 """
str='snooze alarms'
str2="alas,no more Z's"
str=str.lower()
str2=str2.lower()

for x in str:
    if x.isalpha():
        if str.count(x)!=str2.count(x):
            print('not anagrams')
            break
    else:
        print('Anagrams')





