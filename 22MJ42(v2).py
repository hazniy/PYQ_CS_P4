#ques 1 stack
#(a)
StackData = ['' for i in range (10)]
StackPointer = 0
#(b)
def output():
    global StackPointer, StackData, i
    for i in range(10):
        data = StackData[i]
        print(data, StackPointer)
        i = i + 1
        StackPointer = StackPointer + 1
#(c)
def Push(item):
    global StackPointer
    if StackPointer >= 10:
        return False
    else:
        StackPointer = StackPointer + 1
        StackData[StackPointer] = item
        return True
#(d)(i)
#main
for i in range(11):
    ReturnVal = Push(int(input(print('enter a number: '))))
    if ReturnVal == True:
        print('successfully added')
    else:
        print('stack is full')
print(StackData)
#PROBLEM TO ADDRESS : knp takleh guna for dlm this case
#(e) (i)
def Pop():
    global StackPointer
    if StackPointer <= 0:
        return -1
    else:
        data = StackData[StackPointer]
        StackPointer = StackPointer-1
        return data
#(e)(ii)
Pop()
Pop()
print(StackData)
#ques 2 bubble sort 2d Array
#(a)
import random
ArrayData = [[0]*10 for i in range(10)] #integer
for x in range(0, 10):
    for y in range(0, 10):
        ArrayData[x][y] = random.randint(1, 100)
#(b)(i)
ArrayLength = 10
for x in range (0, ArrayLength - 1):
    for y in range (0, ArrayLength - 2) :
        for z in range (0, ArrayLength - y - 2):
            if ArrayData[x][z] > ArrayData [x][z + 1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue
#PROBLEM TO ADDRESS
#knp ms line 11 dia buat (0, Al) instead of (0,Al-1)

#(b)(11)
#main
import random
ArrayData = [[0]*10 for i in range(10)] #integer
for x in range(0, 10):
    for y in range(0, 10):
        ArrayData[x][y] = random.randint(1, 100)
print('before')
print(ArrayData)
ArrayLength = 10
for x in range (0, ArrayLength - 1):
    for y in range (0, ArrayLength - 2) :
        for z in range (0, ArrayLength - y - 2):
            if ArrayData[x][z] > ArrayData [x][z + 1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue
print('after')
print(ArrayData)

#ques 3 text file
#(a)
class Card:
    def __init__(self, Num, Col):
        self.__Number = Num
        self.__Col = Col
#(b)
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Col
#(c)
#main
array = []
try:
    global array
    file = open('C:\ Users\ u\Desktop\CS P4\9618_s22_sf_42.zip\06_9618_42_Confidential Source Files June 2022\CardValues.txt','r')
    for i in range(30):
        num = file.readline()
        col = file.readline()
        array.append(Card(num,col))
    file.close()
except IOError:
    print('file doesnt exist')
#(d)
NumChosen = [False for i in range(30)]
def ChooseCard():
    data = -1
    flag = True
    while flag == True:
        data = int(input(print('input an integer: ')))
        if data < 1 or data > 30:
            print('enter a valid num: ')
        elif NumChosen[data-1] == True:
            print('already taken')
        else:
            print('valid')
            flag = False
    NumChosen[data-1] = True
    return data-1
#(e)(i)
player1 = []
for i in range(4):
    val = ChooseCard()
    player1.append(array[val])
for x in range(4):
    print(player1[x].GetColour())
    print(player1[x].GetNumber())
