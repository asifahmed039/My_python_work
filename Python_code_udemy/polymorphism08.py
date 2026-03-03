#Method Resolution Order
"""
simple
    parent(2)-------childe(1)   order to access methods in class in inheritance

Multilevel
    [A](3)-----[B](2)------[C](1)

Multiple
    [A](2)      [B](3)

        [C](1)

Mixed
        [P](6)

    [A](3)     [X](5)

    [B](2)     [Y](4)

        [C](1)




"""
class Parent:
    def show(self):
        print("patent show")

class child(Parent):
    def show(self):
        print("child show")

c=child()
c.show()
print(child.mro())