#create a class called order which stores item and its price.
#use dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order2

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):     #greater than
        return self.price>ord2.price
ordr1=order("dhips",20)
ordr2=order("tea",15)
print(ordr1>ordr2)#true
        