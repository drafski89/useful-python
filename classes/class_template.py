# Purpose:  Demonstrate a basic class in Python 2

# Basic Template of a Bank Account Class
class BankAccount:
    # Overloaded init function
    # If no starting amount specified, startingAmount = 0
    # If starting amount specified, startingAmount = amount specified
	def __init__(self, startingAmount=0):
        # Set balance to startingAmount
		self.balance = startingAmount
	
    # Balance getter method
    # Purpose:  Get the current balance of the bank account
    # Returns:  Current balance in bank acount
	def getBalance(self):
		return self.balance
	
    # Withdraw method
    # Purpose:  Decrease the bank balance
    # Returns:  New bank account balance amount
	def withdraw(self, withdrawAmount):
		self.balance -= withdrawAmount
		return self.balance
	
    # Deposit method
    # Purpose:  Increase the bank balance
    # Returns:  New bank account balance amount
	def deposit(self, depositAmount):
		self.balance += depositAmount
		return self.balance

# Main method        
if __name__ == "__main__":
    # Create a bank account named "a", balance = 0 by default
    a = BankAccount()
    print "Created a. Balance is:"
    print a.getBalance()
    # Create a bank account named "b", balance = 20
    b = BankAccount(20)
    print "Created b. Balance is:"
    print b.getBalance()
    # Deposit 20 into "b"
    b.deposit(20)
    print "Deposited 20 into b:"
    print b.getBalance()
    # Withdraw 30 from "b"
    b.withdraw(30)
    print "Withdrew 30 from b:"
    print b.getBalance()