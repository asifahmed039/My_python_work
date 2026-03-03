#Rational Number challange
"""
    Add:-
        1/2+2/3=7/6
    Mult:-
        2/6=1/2*2/3
    Compare:-
        1/2<2/3     3<4(numo)

"""
from math import gcd
class Rational:
    def __init__(self,p,q=1):
        self.p=p//gcd(p,q)
        self.q=q//gcd(p,q)
    
    def __add__(self,other):
        num=self.p*other.q+other.p*self.q
        den=self.q*other.q
        return Rational(num,den)
    
    def __mul__(self,other):
        return Rational(self.p*other.p,self.q*other.q)
    
    def __eq__(self,other):
        return self.p==other.p and self.q==other.q
    
    def __lt__(self,other):
        return self.p*other.q<self.q*other.p
    
    def __str__(self):
        if self.q==1:
            return f"{self.p}"
        else:
            return f"{self.p}/{self.q}"
        
r1=Rational(3,4)
r2=Rational(5,6)
print("Addition:",r1+r2)
print("multiplication:",r1*r2)
print(f"{r1}<{r2}",r1<r2)



        