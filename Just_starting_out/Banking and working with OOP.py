class Account():
    
    def __init__(self, owner, balance):
        balance_deposit = int()
        self.owner = owner
        self.balance = balance
    
        
    def deposit(self):
        deposit_amount = int(input('How Much would you like to deposit? '))
        while deposit_amount > 0:
            total_balance =str(deposit_amount + self.balance)
            Account.balance_deposit = total_balance 
            return int(total_balance)
            break

   #next step is for me to keep a count of the new balances after each deposit and to update the balance class
   #Maybe create a class just called Update balance and Use a for loop and empty list to update the list after each deposit or withdraw
   #also need to create a withdraw class that wont over draw the balance. So i need to place a if statement that if X < balance..... 