#Abstract class and interface
""""

"""
from abc import ABC,abstractmethod
class Parent(ABC):
    def meth1(self):
        print("Patent meth--1")
    @abstractmethod
    def meth2(self):
        pass
class Child(Parent):
    def meth3(self):
        print("child meth--3")
    def meth2(self):
        print("meth--2 ")

c=Child()
c.meth2()