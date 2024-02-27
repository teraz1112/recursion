class BankAccount:
    def __init__(self, bankName,ownerName, savings):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
    
    def depositMoney(self, depositAmount):
        if self.savings <= 20000:
            self.savings -= 100
        self.savings += depositAmount
        return int(self.savings)
    
    def withdrawMoney(self, withdrawAmount):
        maxWithdrawAmount = self.savings * 0.2
        if withdrawAmount > maxWithdrawAmount:
            withdrawAmount = maxWithdrawAmount
        self.savings -= withdrawAmount
        return int(self.savings)        
    
    def pastime(self,days):
        return days*0.25+self.savings
    
user1 = BankAccount("Chase", "Claire Simmmons", 30000)
user2 = BankAccount("Bank Of America", "Remy Clay", 10000)

print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))
print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(505))        
