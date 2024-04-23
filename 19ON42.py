#ques 1 OOP
class Employee:
    def __init__(self, ID, name, Address, DOB):
        self.ID = ID
        self.name = name
        self.Address = Address
        self.DOB = DOB
    def GetEmployeeID(self):
        return self.ID
    def SetEmployeeID(self, NewID):
        self.ID = NewID

def SetPension(self, NewPension):
    if NewPension == True or NewPension == False:
        self.__Pension = NewPension
        return True
    else:
        return False
def CalculateMonthlySalary(TheEmployee):
    BonusPayment = 0
    PensionPayment = 0
    HoursBonus = 0.05
    HoursMonthBonus = 160
    PensionCost = 0.04
    PublicHolidayBonus = 0.03
    BasicSalary = TheEmployee.GetMonthlyPayment()
    if TheEmployee.GetHoursThisMonth() >= HoursMonthBonus:
        BonusPayment = BasicSalary * HoursBonus
    if TheEmployee.GetPension() == True:
        PensionPayment = BasicSalary * PensionCost
    if TheEmployee.GetPublicHoliday() == True:
        BonusPayment = BonusPayment + BasicSalary * PublicHolidayBonus
    print("The pension payment is ", str(PensionPayment))
    print("The bonus payment is ", str(BonusPayment))
    MonthlySalary = BasicSalary + BonusPayment - PensionPayment
    return MonthlySalary
