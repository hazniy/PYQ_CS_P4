#Q1
Animals = [] #STRING OF 10
for i in range(10):
    name = input('enter an animal: ')
    Animals.append(name.lower())
print(Animals) #check if the the names in the array or not

def SortDescending():
    ArrayLength = len(Animals)
    for x in range (len(Animals)):
        for y in range(len(Animals)-1):
            if (Animals[y],0,1) < (Animals[y+1],0,1):
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp
SortDescending()
print(Animals) #check after sorting

#q2
class SaleData:
    def __init__(self, id, quantity):
        self.id = id
        self.quantity = quantity
Circularqueue = [] #5 items of SaleData
for i in range(5):
    Circularqueue.append(SaleData('',-1))
Head = 0 #point to first val in the queue
Tail = 0 #point to next empty array
NumOfItems = 0
def Enqueue(newsale):
    global Circularqueue, Head, Tail, NumOfItems
    if NumOfItems == 5:
        return -1
    else:
        if Tail == 5:
            Tail = 0
            Circularqueue[Tail] = newsale
        else:
            Circularqueue[Tail] = newsale
            Tail = Tail + 1
        NumOfItems = NumOfItems + 1
        return 1

def Dequeue():
    global Circularqueue, Head, Tail, NumOfItems
    if NumOfItems == 0:
        return 'null'
    else:
        remove = Circularqueue[Head]
        if Head == 5:
            Head = 0
        else:
            Head = Head + 1
        NumOfItems = NumOfItems - 1
        return remove

def EnterRecord():
    id = input('enter an ID: ')
    quantity = int(input('enter your quantity: '))
    record = SaleData(id,quantity)
    value = Enqueue(record)
    if value == -1 :
        print('full')
    else:
        print('stored')
#main
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
value = Dequeue()
if value == 'null':
    print('no item in queue')
else:
    print('quantity being remove:',value.quantity)
    print('id being remove:',value.id)
EnterRecord()

#q3
#employee has employee num
#employee has a job title
#employee has hourly pay rate
#employee also has paid in a week in 52 week
class Employee:
    def __init__(self, hourpay, empnum, jobtitle):
        self.HourlyPay = hourpay #REAL
        self.EmployeeNumber = empnum #STRING
        self.jobtitle = jobtitle #STRING
        self.PayYear2022 = [0.0 for i in range(52)] #ARRAY OF REAL
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
        total = numhrs * ((self.BonusVal+100)/100 ) #* self.HourlyPay
        Employee.SetPay(self, weeknum, total) #kena mention setpay employee balik

#main (finally)
EmployeeArray = [] #8 employees type Employee
try:
    file = open("C:/Users/u/Desktop/Employees.txt",'r')
    payhour = file.readline().strip()
    while payhour != '':
        empnum = file.readline().strip()
        jobtitle = file.readline().strip()
        if len(jobtitle) <= 5:
            bonusval = jobtitle
            jobtitle = file.readline().strip()
            EmployeeArray.append(Manager(float(payhour),empnum,jobtitle,float(bonusval)))
        else:
            EmployeeArray.append(Employee(float(payhour),empnum,jobtitle))
        payhour = file.readline().strip() #jgn tuka float terus sbb kita nak compare string
    file.close()
except IOError:
    print('file doesnt exist')
print(EmployeeArray)

def Enterhrs():
    try:
        file = open('C:/Users/u/Desktop/HoursWeek1.txt', 'r')
        empnum = file.readline().strip()
        while empnum != '':
            for i in range(8):
                if EmployeeArray[i].GetEmployeeNumber() == empnum:
                    numhrs = float(file.readline().strip())
                    EmployeeArray[i].SetPay(1,numhrs)
            empnum = file.readline().strip()
        file.close()
    except IOError:
        print('file doesnt exist')

#main
Enterhrs()
for i in range(len(EmployeeArray)):
    num = EmployeeArray[i].GetEmployeeNumber()
    print(num)
    TotalPay = EmployeeArray[i].GetTotalPay()
    print(TotalPay)

#datetimme
import datetime

tarikh = datetime.date(2024,5,17)
print(tarikh.month) #print month
print(tarikh.year) #year
print(tarikh.day) #day
