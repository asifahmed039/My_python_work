# Del keyword
"""
    Used to delete object properties or object itself.

    del s1.name
    de s1
"""

class student:
    def __init__(self,name):
        self.name=name

s1=student("moktar")
print(s1.name)
del s1.name  #delete attr
del s1   #delete object
print(s1.name)