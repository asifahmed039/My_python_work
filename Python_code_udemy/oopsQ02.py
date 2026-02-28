#class Bank Account
""""

"""
class InsufficientFundsError(Exception):
    pass
class BankAccount:
    Acc_counter=100
    def __init__(self,name,balance=0):
        self.name=name
        BankAccount.Acc_counter+=1
        self.__acc=BankAccount.Acc_counter
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-+amount
        else:
            raise InsufficientFundsError("Not enough funds")
    def balance(self):
        return self.__balance
    def details(self):
        return self.__acc,self.name,self.__balance
    
james=BankAccount('james',2000000)
asif=BankAccount('Asif',300000000000)
print(asif.details())