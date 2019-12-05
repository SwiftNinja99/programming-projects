class Bank:
    def __init__(self, bankName, custList = None):
        self.bankName = bankName
        if custList is None:
            custList = []
        else:
            self.custList = custList
    def showCustList(self):
        for cust in self.custList:
            cust.__str__()
    def deposit(self, custId, amount):
        for cust in self.custList:
            if cust.getId() == custId:
                acc = cust.getAcc() 
                acc += amount
                cust.setAcc(acc)
    def withdraw(self, custId, amount):
        for cust in self.custList:
            if cust.getId() == custId:
                acc = cust.getAcc() 
                acc -= amount
                cust.setAcc(acc)
    def setPass(self, custId, password):
        for cust in self.custList:
            if cust.getId() == custId:
                cust.setPass(password)
    def addCustomer(self, cust):
        if cust not in self.custList:
            self.custList.append(cust)
    def removeCustomer(self, cust):
        if cust in self.custList:
            self.custList.remove(cust)
    def getAccount(self, custId):
        for cust in self.custList:
            if cust.getId() == custId:
                cust.__str__()
    def getBalance(self, custId):
        for cust in self.custList:
            if cust.getId() == custId:
                return cust.getBalance()
    def setBalance(self, custId, newBal):
        for cust in self.custList:
            if cust.getId() == custId:
                cust.setBalance(newBal)
    def validateId(self, custId):
        for cust in self.custList:
            if cust.getId() == custId:
                return True
        return False
    def validatePass(self, custId, password):
        for cust in self.custList:
            if cust.getId() == custId:
                if cust.getPass() == password:
                    return True
        return False
    def getCustName(self, custId):
        for cust in self.custList:
            if cust.getId() == custId:
                return cust.getName()
    @staticmethod
    def validateOption(option):
        if option in [1, 2, 3, 4, 5, 6]:
            return True
        return False
    @staticmethod
    def showOptions():
        print('''
1) Display balance
2) Deposit money
3) Withdraw money
4) Change password
5) Close account
6) Log out''')
    def getName(self):
        return self.bankName