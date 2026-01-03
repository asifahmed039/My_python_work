#Qustion practice:--



class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit amount
    def  debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("avl bal:",self.get_balance())

    #credit amount
    def  credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
    
    def get_balance(self):
        return self.balance



acc1=account(10000,12345)
print(acc1.balance,acc1.account_no)
print(acc1.debit(2000))



