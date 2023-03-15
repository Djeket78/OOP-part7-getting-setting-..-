
class Bank:
    def veryfity_date(self,balance):
        if type(balance) != int:
            raise TypeError("Only intenger values accepted as balance!!!")
        
    def __init__(self, balance=0):
        self.veryfity_date(balance)
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        self.__balance = balance
            
    def __str__(self):
        return f"BANK: {self.__balance}"
    
class LocalBank(Bank):
    def __init__(self, locality, balance = 0):
        super().__init__(balance) 
        self.locality = locality
        
    def __str__(self):
        return f"LOCAL BANK({self.locality}): {self.getBalance()}"
    
class CreditBank(Bank):
    def __init__(self, procent, credit, balance = 0):
        super().__init__(balance) 
        self.procent = procent
        self.__credit = credit
        if type(credit) != int:
            raise TypeError("Only intenger values accepted as credit!!!")
        if credit > 50_000:
            raise TypeError("Сredit limit up to 50000!!!")
        
    def getBalance(self):
        return self.__credit
    
    def setBalance(self, credit):
        self.__credit = credit
        
    def __str__(self):
        return f"CREDIT BANK: {self.getBalance()}; credit: {self.__credit}; at {self.procent} percent the amount per annum {self.__credit*self.procent/100}"
    
    ######################################################################
    
world_bank = Bank(1_000_000_000_000)
    
agro  = LocalBank("Chisinau", 1_000_000)
credit  = CreditBank(5, 5000, 1_000_000)
    
    
print(world_bank)
print(agro)
print(credit)