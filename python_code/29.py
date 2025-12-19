#function in python
"""
    Block of statements that perform a specific task.
        #function definition
        def func_name(param1,param2...):
            #some work
            return val
        
        #function call
            fun_name(arg1,arg2..)

"""
def cal_sum(a,b,c=0):      #function definition
    sum=a+b                 #user define function
    print(sum)

#02 
def print_hello():
    return "hello"

cal_sum(10,10)             #function call , arguments
#reusibility properties
cal_sum(30,10)
cal_sum(50,10)

str=print_hello()
print(str)

#average of 3 numbers
def cal_avg(a,b,c):
    avg=(a+b+c)/3
    return avg

print(cal_avg(10,20,30))
