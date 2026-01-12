#complex number
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show_number(self):
        print(self.real,"i+",self.img,"j")
#normal logic without dunder function
    # def add(self,num2):
    #     newReal=self.real+num2.real
    #     newImg=self.img+num2.img
    #     return complex(newReal,newImg)
#dunder function
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal,newImg)
#subtrcation using dunder function
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return complex(newReal,newImg)


    
    
num1=complex(1,3)
num1.show_number()
num2=complex(4,6)
num2.show_number()
# sum=num1.add(num2)
# num3=num1+num2
num3=num2-num1
print(num3.show_number())