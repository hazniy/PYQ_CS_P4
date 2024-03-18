Animals = ['' for i in range(10)]
Animals[0] = 'horse'
Animals[1] = 'lion'
Animals[2] = 'rabbit'
Animals[3] = 'mouse'
Animals[4] = 'bird'
Animals[5] = 'deer'
Animals[6] = 'whale'
Animals[7] = 'elephant'
Animals[8] = 'kangaroo'
Animals[9] = 'tiger'


def sortdescending():
    arrayLength = len(Animals)
    for X in range(arrayLength-1):
        for Y in range(arrayLength-X-1):
            if Animals[Y] < Animals[Y+1]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y+1]
                Animals[Y+1] = Temp
#main
sortdescending()
for i in range(10):
    print(Animals[i])

class SaleData():
    def __init__(self,ID, Quantity):
        self.ID = ID
        self.Quantity = Quantity
CircularQueue = []
for i in range(5):
    Temp = SaleData('',-1)
    CircularQueue.append(Temp)
Head = 0
Tail = 0
NumberOfItems = 0
#----------------------------------------------------------
def Enqueue(newrecord):
    global Head,Tail,NumberOfItems,CircularQueue
    if NumberOfItems >= 5:
        print('queue is full')
        return -1
    else:
        Tail = Tail + 1
        if Tail > 4:
            Tail = 0
        CircularQueue[Tail] = newrecord
        NumberOfItems = NumberOfItems + 1
        return 1
def Dequeue():
    global Head, Tail, NumberOfItems, CircularQueue
    if NumberOfItems <= 0 :
        print('Queue is empty')
        return ''
    else:
        remove = CircularQueue[Head]
        Head = Head + 1
        NumberOfItems = NumberOfItems - 1
        if Head > 4:
            Head = 0
        print(CircularQueue[Head])
        return CircularQueue[Head]
def EnterRecord():
    ID = input('enter an ID: ')
    Quantity = int(input('enter quantity: '))
    Data = SaleData(ID, Quantity)
    Return = Enqueue(Data)
    if Return == -1 :
        print('full')
    else:
        print('stored')

class Employee():
    def __init__(self, pay, num, title):
        self.HourlyPay = pay #REAL
        self.EmployeeNumber = num #STRING
        self.JobTitle = title #STRING
        self.PayYear2022 = [0.0 for i in range(51)] #REAL
    def GetEmployeeNumber(self):
        return self.EmployeeNumber
    def SetPay(self, weeknum, numhours):
        total = weeknum * numhours
        flag = False
        i = 0
        while flag == False:
            if self.PayYear2022[i] == 0.0:
                self.PayYear2022 = total
                flag = True
    def GetTotalPay(self):
        for i in range(51):
            while self.PayYear2022[i] != 0.0:
                print(self.PayYear2022[i])
                return self.PayYear2022
class Manager(Employee):
    def __init__(self, pay, num, val, title):
        Employee.__init__(self, pay, num, title)
        self.BonusValue = val #REAL
    def SetPay(self, weeknum, numhours):
        newhours = numhours + (numhours * self.BonusValue/100)
        Employee.SetPay(self,weeknum,newhours)
#main
EmployeeArray = []
try:
    file = open('C:/Users/N129ALS22030/Desktop/Employees.txt', 'r')
    i = 0
    pay = file.readline()
    num = file.readline()
    bonus = file.readline()
    if float(bonus) == float:
        title = file.readline()
        temp = Manager(pay,num,bonus,title)
        EmployeeArray.append(temp)
    else:
        temp = Employee(pay,num,bonus)
        EmployeeArray.append(temp)
    file.close()
except IOError:
    print('file doesnt exist')

def EnterHours():
    try:
        hoursfile = open('C:/Users/N129ALS22030/Desktop/HoursWeek1.txt', 'r')
        num = hoursfile.readline()
        for i in range(len(EmployeeArray)):
            if num == EmployeeArray[i].GetEmployeeNumber():
                hours = hoursfile.readline()
                EmployeeArray[i].SetPay(EmployeeArray[i].HourlyPay, hours)
        file.close()
    except IOError:
        print('file doesnt exist')
#amend main
EnterHours()
for i in range(len(EmployeeArray)):
    num = EmployeeArray[i].GetEmployeeNumber()
    print(num)
    TotalPay = EmployeeArray[i].GetTotalPay()
