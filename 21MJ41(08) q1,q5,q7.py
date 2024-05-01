#ques 1 OOP
class fooditem:
    def __init__(self, name, code, cost):
        self.name = name
        self.code = code
        self.cost = cost
    def getcode(self):
        return self.code
    def getcost(self):
        return self.code
    def getname(self):
        return self.name

class vendingMachine:
    def __init__(self, item1, item2, item3, item4):
        self.items = []
        self.items.append(item1)
        self.items.append(item2)
        self.items.append(item3)
        self.items.append(item4)
        self.moneyIn = 0

def checkValidCode(code):
    for x in range (4):
        if items[x].getcode == code:
            if self.items[x].getcost <= self.moneyIn:
               return x
            else:
                return -2
    return -1
machineOne = vendingMachine(chocolate, sweets, sandwich, apple)

#ques 5 binary search RECURSION
# (b)
def recursiveBinarySearch(lowerbound, upperbound, searchValue):
    mid = lowerbound + int((upperbound - lowerbound)/2)
    if upperbound < lowerbound:
        return -1
    else:
        if dataArray[mid] < searchValue:
            return recursiveBinarySearch(mid + 1, upperbound, searchValue)
        elif dataArray[mid] > searchValue:
            return recursiveBinarySearch(lowerbound, mid - 1, searchValue)
        else:
            return mid

#PROBLEM TO ADDRESS
#why mid kena guna formula tu, kalau buat highest+lowest / 2? <-- rasa tak kesah pon
#tak faham the flow of recursive

#ques 7 stack
#(a)
def setupstack(stackarray,tail):
    for i in range (999):
       stackarray[i] = -1
    tail = -1
#(b)
def pop(stackarray, tail):
    if tail < 0:
        return -1
    else:
       datatoreturn = stackarray[tail]
       tail = tail - 1
       return datatoreturn
