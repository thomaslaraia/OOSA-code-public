import numpy as np

class yourBank(object):
    # attribute
    numb_accounts=0

    def __init__(self,name,balance):
        print(f"Creating account '{name}'")
        self.name=name
        self.balance=balance
        yourBank.numb_accounts+=1

    def deposit(self,amt):
        self.balance+=amt
    def withdraw(self,amt):
        self.balance-=amt
    def inquiry(self):
        return self.balance
    def tax(self,rate):
        self.balance-=self.balance*rate
    def deposit_1000(self):
        self.balance+=1000

class evilBank(yourBank):
    def inquiry(self):
        p = np.random.random(1)[0]
        
        if p<= 0.5:
            return self.balance*1.2
        else:
            return self.balance

if __name__ == '__main__':
    y = evilBank("Thomas",0)
    y.deposit(5.0)
    print(y.inquiry())
    #print(yourBank.numb_accounts)
