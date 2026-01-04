#Multiple Inheritence
class A:
    varA="welcome"
class B:
    varB="Person"
class C(A,B):
    varC="hello.."

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)