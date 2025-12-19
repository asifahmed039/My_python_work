#Relational operator
a=50
b=20
print(a==b)#false
print(a!=b)#true
print(a>=b)#true
print(a<=b)#false
print(a>b)#true
print(a<b)#false
#Assignment operator
num=10
num+=105 #also use [num=num+105] [num*=10,num%=10, num/=5,num-=10]
print("num : ",num)
#Logical operator [not or and]
print(not False)
print(not (a>b))
#and operator 
val1=False
val2=True
print("and operator : ", val1 and val2)
print("or operator : ", val1 or val2)

#Type converstion
""" a,b=1,2.2
sum=a+b no error in float
 compiler implicitly convert the result into greater data type 
 but
 a,b=4,"2" its give error
 sum=a+b
 """ 
#implicit conversion
a=2
b=4.25
sum=a+b #2.0+4.25=>6.25
#Type casting do manually
d,b=1,"2"#"sunny" give error during conversion
c=int(b)
sum=d+c

a=3.14
a=str(a)
print(type(a))






