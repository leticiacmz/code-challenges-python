class Account:
    def __init__(self, number, holder, balance, limit):
        print(f"Created bank account object... {self}")
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        
    def bank_statement(self):
        print(f"Bank statement: {self.__balance}\nHolder of the account: {self.__holder}")      
        
    def cash_deposit(self, value):
        self.__balance += value
    
    def withdraw_money(self, value): 
        self.__balance -= value
        
    def bank_transfer(self, value, destiny):
        self.withdraw_money(value)
        destiny.cash_deposit(value)
    
    @property
    def limit(self):
        return self.__limit   
    
    @property 
    def balance(self):
        return self.__balance
    
    @property
    def holder(self):
        return self.__holder
    
    def set_limit(self, new_limit):
        self.__limit =  new_limit