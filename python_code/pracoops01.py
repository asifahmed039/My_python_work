class bank:
    bank_name='Tech bank of world'
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account=account_no

    #debit amount from account
    def debit_amount(self,amount):
        self.balance-=amount
        print('avl balance=',self.balance)

    #credit amount in account
    def credit_amount(self, amount):
         self.balance+=amount
         print('avl balance=',self.balance)

a1=bank(100,7494)
a1.credit_amount(50)
print(a1.balance)
del a1.balance
print(a1.balance)


        


        