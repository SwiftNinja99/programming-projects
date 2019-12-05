class Customer:
    def __init__(self, custId, custName, password, balance):
        self.custId = custId
        self.custName = custName
        self.password = password
        self.balance = balance
    def getId(self):
        return self.custId
    def getName(self):
        return self.custName
    def getPass(self):
        return self.password
    def getBalance(self):
        return self.balance
    def setId(self, id):
        self.custId = id
    def setName(self, name):
        self.custName = name
    def setPass(self, password):
        self.password = password
    def setBalance(self, balance):
        self.balance = balance
    def __str__(self):
        print("ID =", self.custId, "\tName =",self.custName, "\tbalance =", self.balance)