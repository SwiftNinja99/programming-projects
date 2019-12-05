'''This program emulates a bank application program. It asks the user to enter their user ID and
password. It verifies correctness and displays the appropriate message. It has the following 
functions: 
Displays account balance, deposit amount, withdraw amount, change password, and logout
This program does full error handling, including runtime errors.
'''
from custClass import Customer
from bankClass import Bank
print
print("Bank Application")
print

jsmith = Customer('jsmith', 'John Smith', 'jsmith360', 10)
jdoe = Customer('jdoe', 'Jane Doe', 'jdoe360', 9)
jarch = Customer('jarch', 'John Arch', 'jarch360', 8)
mallen = Customer('mallen', 'Mary Allen', 'mallen360', 7)

bank = Bank('John\'s Bank', [jsmith,jdoe,jarch])
bank.addCustomer(mallen)

while True:
    
    userID = input("Please enter your user ID: ")
    if not bank.validateId(userID):
        print("\nInvalid user ID, please try again")
    else:
        password = input("Please enter your password: ")
        if not bank.validatePass(userID, password):
            print("\nInvalid password, try again.")
        else:
            print("\nWelcome to", bank.getName() +"!")
            while True:
                try:
                    bank.showOptions()
                    op = int(input("Select the number that reflects your desired option:"))
                    if not bank.validateOption(op):
                        print("\nInvalid option, please select a number from the above list: ")
                    elif op == 1:#display balance
                        print("\nYour balance is:", bank.getBalance(userID))
                    elif op == 2:#deposit
                        amount = float(input("Enter the amount you wish to deposit: "))
                        if amount<0:
                            print("\nYou cannot deposit a negative amount.")
                        else:
                            amount += bank.getBalance(userID)
                            bank.setBalance(userID, amount)
                            print("\nThe new balance is", bank.getBalance(userID))
                    elif op == 3:#withdraw
                        amount = float(input("Enter the amount you wish to withdraw: "))
                        if amount<0:
                            print("\nYou cannot withdraw a negative amount.")
                        elif amount > bank.getBalance(userID):
                            print("\nInsufficient funds.")
                        else:
                            amount = bank.getBalance(userID) - amount
                            bank.setBalance(userID, amount)
                            print("\nThe new balance is", bank.getBalance(userID))
                    elif op == 4:#change password
                        newPass = input("Please enter your new password: ")
                        checkPass = input("Re-enter your passsword: ")
                        if newPass != checkPass:
                            print("\nPasswords do not match")
                        else:
                            bank.setPass(userID, newPass)
                            print("\nYour password has been set!")
                    elif op == 5:#remove accounts
                        if bank.getBalance(userID) == 0:
                            bank.removeCustomer(userID)
                            print("\nYour account has been successfully terminated.")
                            break
                        else:
                            print("You cannot close an account with funds. You currently have $"+bank.getBalance(userID))
                    elif op == 6:#log out
                        print("\nLogged out, bye", bank.getCustName(userID))
                        break
                except:
                    print("\nYou did not enter a valid number, please try again.")