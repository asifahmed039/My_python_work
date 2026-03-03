#Inventory Tracker challenge
""" 
we can also define our own dictionary in python
    collection module
    
"""
from collections import UserDict

class Inventory(UserDict):
    def __init__(self):
        super().__init__()

    def __setitem__(self,item,qty):
        if not isinstance(item,str) or not isinstance(qty,int):
            raise Exception('Product quantity must be integer and string')
        super().__setitem__(item.lower(),qty)

    def __getitem__(self,item):
        return super().__delitem__(item.lower())
    
    def __delitem__(self, item):
        return super().__delitem__(item.lower())

    def __contains__(self,item):
        return super().__contains__(item.lower()) 

    def update_stock(self,item,qty):
        if item in self:
            self[item]+=qty
        else:
            self[item]=qty

Inventory1=Inventory()
Inventory1['Apple']=10
Inventory1.update_stock("apple",-1)
print(Inventory1['Apple'])   