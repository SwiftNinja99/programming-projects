
print("----------------------------------------------------")
print("                   Calculator")
print("----------------------------------------------------")
print("+  --> to add")
print("-  --> to subtract")
print("*  --> to multiply")
print("/  --> to divide")
print("** --> to exponentiate")
print("E  --> to end the program")
op = "+"
valid_op=['+','-','*','/','**']
while op != "E":
  op=input("\nEnter the operation from the selections above:")
  if op in valid_op:
    try:
      n1=float(input("Enter your first number:"))
      n2=float(input("Enter your second number:"))
      if op=="+":
        answer=n1+n2
      elif op=="-":
        answer=n1-n2
      elif op=="*":
        answer=n1*n2
      elif op=="/":
        answer=n1/n2
      elif op=="**":
        answer=n1**n2
      print(n1,op,n2,"=",answer)
    except:
      print("Invalid Number. Do it again!")
  elif op != "E":
    print("\nInvalid selection. Try again!")