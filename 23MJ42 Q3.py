#employee has employee num
#employee has a job title
#employee has hourly pay rate
#employee also has paid in a week in 52 week
class Employee:
    def __init__(self, hourpay, empnum, jobtitle):
        self.HourlyPay = hourpay
        self.EmployeeNumber = empnum
        self.PayYear2022 = jobtitle
        self.PayYear2022 = []
        for i in range(52):
            self.PayYear2022[i] = 0.0
    def GetEmployeeNumber(self):
        return self.EmployeeNumber
    def SetPay(self, weeknum, numhrs):
        total = numhrs * self.HourlyPay
        self.PayYear2022[weeknum] = total
    def GetTotalPay(self):
        total = 0
        for i in range(52):
            total = total + self.PayYear2022[i]
        return total

#manager gets bonus in percentage
#calc pay = numhrs * bonus val
class Manager(Employee):
    def __init__(self, hourpay, empnum, jobtitle, bonusval):
        Employee.__init__(self, hourpay, empnum, jobtitle)
        self.BonusVal = bonusval
    def SetPay(self, weeknum, numhrs):
        total = numhrs * ((self.BonusVal+100)/100 ) * self.HourlyPay
        self.PayYear2022[weeknum] = total

#main (finally)
EmployeeArray = [] #8 employees type Employee
try:
    file = open('C:/Users/u/Desktop/Employees.txt','r')
    payhour = float((file.readline()).strip())
    while payhour != '':
        empnum = int((file.readline()).strip())
        jobtitle = file.readline()
        if len(jobtitle) <= 5:
            bonusval = float(jobtitle)
            jobtitle = file.readline().strip()
            EmployeeArray.append(Manager(payhour,empnum,jobtitle,bonusval))
        else:
            EmployeeArray.append(Employee(payhour,empnum,jobtitle))
        payhour = float(file.readline().strip())
    file.close()
except IOError:
    print('file doesnt exist')
print(EmployeeArray)

def Enterhrs():
    try:
        file = open('C:/Users/u/Desktop/HoursWeek1.txt', 'r')
        empnum = int(file.readline().strip())
        while empnum != '':
            for i in range(8):
                if EmployeeArray[i].EmployeeNumber == empnum:
                    numhrs = int(file.readline())
                    EmployeeArray[i].SetPay(EmployeeArray[i].PayYear2022,numhrs)
            empnum = int(file.readline().strip())
        file.close()
    except IOError:
        print('file doesnt exist')

#main
Enterhrs()
for i in range(len(EmployeeArray)):
    num = EmployeeArray[i].GetEmployeeNumber()
    print(num)
    TotalPay = EmployeeArray[i].GetTotalPay()
