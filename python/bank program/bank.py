'''This program emulates a bank application program. It asks the user to enter their user ID and
password. It verifies correctness and displays the appropriate message. It has the following 
functions: 
Displays account balance, deposit amount, withdraw amount, change password, and logout
This program does full error handling, including runtime errors.
'''

print
print("Bank Application")
print

database = {
    'jsmith':{'name':"John Smith",  'password':'jsmith360','balance': 100000},
    'jdoe'  :{'name':"Jane Doe",    'password':'jdoe360',  'balance': 90000},
    'jarch' :{'name':"John Arch",   'password':'jarch360', 'balance': 80000}
}
validOptions = list(range(1,6))

error = True
while error:
    error = False
    userID = input("Please enter your user ID: ")
    if userID not in database:
        print('Invalid user ID, please try again.')
        error = True
    else:
        password = input("Please enter your password: ")
        for key in database:
            if key == userID:
                if database[userID]['password'] != password:
                    print("Invalid password, please try again.")
                    error = True
                else:
                    while True:
                        print('''\nWelcome to Viraj's Bank!
1) Display balance
2) Deposit money
3) Withdraw money
4) Change password
5) Log out''')
                        try:
                            op = int(input("Select the option you wish to preform: "))
                            if op not in validOptions:
                                print("\nInvalid option, select from the list above.")
                            elif op == 1:
                                print("\nYour balance is:", database[userID]['balance'])
                            elif op == 2:
                                amount = float(input("Enter the amount you wish to deposit: "))
                                if amount<0:
                                    print("\nYou cannot deposit a negative amount.")
                                else:
                                    database[userID]['balance'] += amount
                                    print("\nThe new balance is", database[userID]['balance'])
                            elif op == 3:
                                amount = float(input("Enter the amount you wish to withdraw: "))
                                if amount<0:
                                    print("\nYou cannot withdraw a negative amount.")
                                elif amount > database[userID]['balance']:
                                    print("\nInsufficient funds.")
                                else:
                                    database[userID]['balance'] -= amount
                                    print("\nThe new balance is", database[userID]['balance'])
                            elif op == 4:
                                newPass = input("Please enter your new password: ")
                                checkPass = input("Re-enter your passsword: ")
                                if newPass != checkPass:
                                    print("\nPasswords do not match")
                                else:
                                    database[userID]['password'] = newPass
                            elif op == 5:
                                print("\nLogged out, bye", database[userID]['name'])
                                break
                        except:
                            print("\nYou did not enter a valid number, please try again.")