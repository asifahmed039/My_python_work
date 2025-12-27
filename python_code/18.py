#set in python
""" 
 Set is the collection of the unordered items.
 Each element in the set must be unique & immutable.
 ex:--
  nums={1,2,3,4}
   set2={1,2,,2,2}  #repeated elements stored only once, so it resolved to {1,2} 
    
    null_set=set()   #empty set syntax

    """

collection={1,2,2,2,"hello","world""world",4}
print(collection)  # set is unordered 
print(len(collection)) #its give 5 repetition items count only once.

queue={}  #empty dictionary notation
demo=set()   #empty set
# list=[]
# print("enter no:") 
# for i in range(0,4,1):
#     list.append(int(input()))
# print(list)
"""
set methods
01)set.add(el)  #adds an element
02)set.remove(el) #removes the element
03)set.clear()  #empties the set
04)set.pop()   #removes a random value

immutable-------->hash value
(hashable)

unhashable-----> did,lists,set
"""

#add(el)
demo.add(1)
demo.add(2)
demo.add(3)
demo.add(4)
# demo.add([12,34,56,87])   #give error list is mutable
demo.add((10,20,30))  #allowed because tupel is immutable.
print(demo)
print(len(demo))

demo1={"hello","asifaischool","world","coding","python"}
print(demo1.pop())
print(demo1.pop())
print(demo1)

"""
05)set.union(set1)  #combine both set values & returns new
06)set.intersection(set2)  #combines common values & returns new

same as mats sets
set1={1,2,3}  set2={3,4,5}
union={1,2,3,4,5}

"""

set1={1,2,3}  
set2={3,4,5}
#union
print(set1.union(set2))  #{1,2,3,4,5}  return new set
print(set1)
print(set2)
#intersection
print(set1.intersection(set2)) #{3}







