class Account():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
        
    def deposit(self):
        deposit_amount =float(input('How Much would you like to deposit? '))
        
        if deposit_amount > 0:
            self.balance += deposit_amount
            print("\n Amount Deposited: ", deposit_amount, "\n Your new balance: ", self.balance)
            break 
   
    def withdraw(self):
        withdraw_amount =float(input('How Much would you like to Withdraw? '))
        
        if self.balance >= withdraw_amount: 
            self.balance -= withdraw_amount
            print("\n Amount Withdrawn: ", withdraw_amount, "\n Your new balance: ", self.balance)
             
        else:
            print ( "\n Insufficient Balance  ")
            
#all finished!!! 
#I need to remeber to use the += cause i made it so much more complicated than it needed to be. 
#I was trying to create a list of all the past deposits and then iterate through that list and then readd the list to get the new balance. Dont be dumb. Seriously think simply