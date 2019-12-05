from calcClass import Calc

print("----------------------------------------------------")
print("                   Calculator")
print("----------------------------------------------------")
calc = Calc()

while True:
    calc.displayOptions()
    op=input("\nEnter the operation from the selections above:")
    if op.upper() != "E":
        if not calc.validOption(op):
            print("\nInvalid operator, please select from the list above")
        else:
            n1=input("Enter your first number:")
            n2=input("Enter your second number:")
            result = calc.calcResult(n1, n2, op)
            if result != False:
                print("\n"+n1,op,n2,"=",result)
            else:
                print("\nInvalid number or undetermined result, please try again.")
    else:
        print("\nGoodbye!")
        break