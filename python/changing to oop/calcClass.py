class Calc:
    def __init__(self):
        pass
    @staticmethod
    def validOption(option):
        validOps = ['+','-','*','/','**']
        if option in validOps:
            return True
        return False
    @staticmethod
    def displayOptions():
        print("\n+  --> to add")
        print("-  --> to subtract")
        print("*  --> to multiply")
        print("/  --> to divide")
        print("** --> to exponentiate")
        print("E  --> to end the program")
    @staticmethod
    def calcResult(n1, n2, op):
        try:
            float(n1)
            float(n2)
            result = eval("("+n1+")"+op+"("+n2+")")
            return result
        except:
            return False