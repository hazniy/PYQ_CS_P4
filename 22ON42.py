#ques 1 insertion
def Initialise():
 global Jobs
 global NumberOfJobs
 for x in range(0, 100):
 Jobs.append([-1,-1])
 NumberOfJobs = 0

def AddJob(JobNumber, Priority):
 global NumberOfJobs
 global Jobs
 if NumberOfJobs == 100:
 print("Not added")
 else:
 Jobs[NumberOfJobs] = [JobNumber, Priority]
 print("Added")
 NumberOfJobs = NumberOfJobs + 1

def PrintArray():
 global Jobs
 global NumberOfJobs
 for X in range(0, NumberOfJobs):
 print(str(Jobs[X][0]), " priority ", str(Jobs[X][1]))

def InsertionSort():
 global Jobs
 global NumberOfJobs
 for I in range(1, NumberOfJobs):
 Current1 = Jobs[I][0]
 Current2 = Jobs[I][1]
 while I > 0 and Jobs[I-1][1] > Current2:
 Jobs[I][0] = Jobs[I-1][0]
 Jobs[I][1] = Jobs[I-1][1]
 I = I - 1
 Jobs[I][0] = Current1
 Jobs[I][1] = Current2

#ques 2 OOP / Text File
#(a)
class Character:
    def __init__(self, Name, Xcoor, Ycoor):
        self.__Name = Name
        self.__XCoor = Xcoor
        self.__YCoor = Ycoor
#(b)
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoor
    def GetY(self):
        return self.__YCoor
#(c)
    def ChangePosition(self, Xchange, Ychange):
        self.__XCoor = self.__XCoor + Xchange
        self.__YCoor = self.__YCoor + Ychange
#(d) & (e)
#main
Game = []
try:
    file = open('C:\ Users\ u\Desktop\CS P4\9618_w22_sf_42.zip\11_9618_42_Confidential Source Files November 2022\Characters.txt', 'r')
    for i in range(10):
        name = file.readline()
        Xcoor = file.readline()
        Ycoor = file.readline()
        Temp = Character(name, int(Xcoor), int(Ycoor))
        Game.append(Temp)
    file.close()
except IOError:
    print('file doesnt exist')
flag = False
while flag == False:
    item = input(print('enter characters name: '))
    for x in range(10):
        if item == Game.GetName[i]:
            print(i)
            flag = True
#PROBLEM TO ADDRESS :
#


#ques 3 queue & recursive
#(a)
queue = [0*100 for i in range(100)] #integer
head = 0 #integer #point first number
tail = 0 #integer #point next free space
#(b)
numitem = 0
def enqueue (newdata):
    global head, tail, numitem
    if numitem == 0:
        return False
    else:
        queue[tail] = newdata
        if tail == 100:
            tail = 0
        tail = tail + 1
        numitem = numitem + 1
        return True
#(c)
#main
for i in range (0,20):
    success = enqueue(i)
    if i == False:
        print('unssuccessful')
    else:
        print('successful')
#(d)
#wrong
total = 0
def iterativeOutput (start):
    global total
    for count in range (start-1, head-1):
        total = total + queue[count]
    return total

#right
def RecursiveOutput (start):
    if (start == 0):
        return queue[start]
    else:
        return queue[start] + RecursiveOutput(start - 1)
#(e)
#main
#wrong
num = int(input('enter an integer: '))
iterativeOutput(num)
print(num)

#right
print(str(RecursiveOutput(tail-1)))
