#recursion in python
"""
   When a function calls itslef repeatedly.
   #prints n to 1 backwards
      def show(n):
         if(n==0):   #base case
            return
         print(n)
         show(n-1)   #function call
   
"""

def number(n):
    if(n==0):
        return
    print(n,end=" ")
    number(n-1)
    #print(n)
number(10)
#write a recursive program to calculate the sum of first n natural numbers.
def sum(n):
   if(n==0):
      return 0
   return n+sum(n-1)

print(sum(10))

#write a recursive function to print all elements in a list.
#hint:Use list & index as parameters

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
   
list=["mango","apple","banana","grapes"]

print_list(list)

    