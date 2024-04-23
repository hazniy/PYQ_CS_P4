#ques 1 OOP
class PrintAccount:
    def __init__(self, FirstN, LastN, ID):
        self.FirstName = FirstN
        self.LastName = LastN
        self.PrintId = ID
        self.credits = 50
    def Getname(self):
        return self.FirstName + '' + self.LastName
    def GetPrintID(self):
        return self.PrintId
    def SetFirstName(self, FirstName):
        self.FirstName = FirstName
    def SetLastName(self, LastName):
        self.LastName = LastName
    def SetPrintID(self, ID):
        self.PrintId = ID
    def AddCredits(self, cash):
        CreditPerDollar = 25
        FreeCredit10 = 25
        FreeCredit20 = 50
        Twenty = 20
        Ten = 10
        if cash >= Twenty:
            Credits = self.credits + (cash * CreditPerDollar) + FreeCredit20
        elif cash >= Ten:
            Credits = self.credits + (cash * CreditPerDollar) + FreeCredit10
        else:
            Credits = self.credits + (cash * CreditPerDollar)
    def RemoveCredis(self):
        self.credits = self.credits - 1
def CreateID(firstname, lastname):
    count = 0
    PrintID = firstname[0:3].lower() + lastname[0:3].lower() + "1"
    StudentAdd = 0
    if count != 0:
        for x in range(count):
            if count[x].getPrintID() == PrintID:
                PrintID = PrintID + 1
                PrintID = firstname[0:3].lower() + lastname[0:3].lower + str(PrintID)
        studentAdd = count
    count[studentAdd] = print(firstname, lastname, PrintID)
    count = count + 1
