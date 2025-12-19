#wap to check if a list contains a palindrome of elements.(hint:use copy() method)
"""[1,2,3,2,1]     copy [1,2,3,2,1]    revesre   [1,2,3,2,1]
"""

list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")

#wap to count the number of students with the "A" grade in the following tuple.
grade=("c","d","a","a","b","b","a")
print(grade.count("a"))

#store the above values in a list & sort them from "a" to "d".
grade1=["c","d","a","a","b","b","a"]
grade1.sort()
print(grade1)
