#global StackData, StackPointer
StackData = [0 for i in range(10)] #INTEGER
StackPointer = 0 #INTEGER

def output():
    for i in range(10):
        print(StackData[i])
    print('stack pointer',StackPointer)

def Push(val):
    global StackPointer
    if StackPointer >= 10:
        print('stack is full')
        return False
    else:
        StackData[StackPointer] = val
        StackPointer = StackPointer + 1
        return True
#main
for i in range(11):
    Data = int(input('enter a number: '))
    val = Push(Data)
    if val == True:
        print('success added')
    else:
        print('not a success')
output()
#Screenshot#

def pop():
    global StackPointer
    if StackPointer == 0:
        print('stack empty bro')
        return -1
    else:
        Remove = StackData[StackPointer - 1]
        StackData[StackPointer - 1] = 0
        StackPointer = StackPointer - 1
        return Remove

#amend main
pop()
pop()
output()
#Screenshot#

import random
#main
ArrayData = [[0]*10 for i in range(10)] #integer
for i in range(10):
    for j in range(10):
        ArrayData[i][j] = random.randint(1,100)

def Output():
    for i in range(10):
        for j in range(10):
            print(ArrayData[i][j], '', end='')
        print()
print('before sorting')
Output()
print()

ArrayLength = 10
for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength-1):
        for Z in range(0, ArrayLength - Y - 1):
            if(ArrayData[X][Z] > ArrayData[X][Z+1]):
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue
print('After sorting')
Output()
print()

#screenshot#

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = int((Lower + (Upper - 1)) /2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1

val = int(input('enter a number: '))
print(BinarySearch(ArrayData,0,10,val))

#screenshot#
class Card:
    def __init__(self, Num, Col):
        self.__Number = Num #INTEGER
        self.__Colour = Col #STRING
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

ArrayCards = [Card(0,'') for i in range(30)] #Card
try:
    file = open('CardValues.txt', 'r')
    for i in range(30):
        numread = int(file.readline())
        colread = file.readline().strip()
        ArrayCards[i] = Card(numread,colread)
    file.close()
except IOError:
    print('file doesnt exist')

Num = [False for i in range(30)] #BOOLEAN
def ChooseCard(): #RETURNS INTEGER
    global Num
    Alr = True
    while Alr == True:
        cardNum = int(input('enter card number 1-30: '))
        if cardNum < 1 or cardNum > 30:
            print('out of range')
        elif Num[cardNum-1] == True:
            print('num alr used')
        else:
            Num[cardNum-1] = True
            print('its a valid num')
            Alr = False
    return cardNum-1

Player1 = [] #card
for i in range(4):
    num = ChooseCard()
    Player1.append(ArrayCards[num])
for j in range(4):
    print(Player1[j].GetNumber())
    print(Player1[j].GetColour())
