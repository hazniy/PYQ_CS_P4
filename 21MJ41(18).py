#ques 1 linked list
class node:
 def __init__(self, theData, nextNodeNumber):
    self. Data = theData
    self.nextNode = nextNodeNumber

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6), node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5

def outputNodes(linkedList, currentPointer):
    while(currentPointer != -1):
        print(str(linkedList[currentPointer].Data))
        currentPointer = linkedList[currentPointer].nextNode

def addNode(linkedList, currentPointer, emptyList):
    dataToAdd = input("Enter the data to add")
    if emptyList <0 or emptyList > 9:
        return False
    else:
        newNode = node(int(dataToAdd), -1)
        linkedList[emptyList] = (newNode)
        previousPointer = 0
        while(currentPointer != -1):
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        return True

#main
outputNodes(linkedList, startPointer)
returnValue = addNode(linkedList, startPointer, emptyList)
if returnValue == True:
 print("Item successfully added")
else:
 print("Item not added, list full")
outputNodes(linkedList, startPointer)

#ques 2 linear search and bubble
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(searchValue):
 for x in range(10):
    if arrayData[x] == searchValue:
        return True
 return False

searchValue = int(input("Enter the number to search for"))
returnValue = linearSearch(searchValue)
if returnValue == True:
 print("It was found")
else:
 print("It was not found")


def bubbleSort():
    for x in range(0, 10):
        for y in range(0, 9):
            if theArray[y] < theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp

#ques 3 oop // text file
#(a)
class TreasureChest:
    # __question : STRING
    # __answer : INTEGER
    # __points : INTEGER
    def __init__(self, ques, ans, points):
        self.__question = ques
        self.__answer = ans
        self.__points = points
# (c)(i)
    def getQuestion(self):
        return self.__question
# (c)(iii)
    def getPoints(self, attempt):
        if attempt == 1:
            return self.__points
        elif attempt == 2:
            return int(self.__points / 2)
        elif (attempt == 3) or (attempt == 4):
            return int(self.__points / 4)
        else:
            return 0
# (c)(ii)
    def checkAnswer(self, ans):
        if ans == self.__answer:
            return True
        else:
            return False
#(b)
arrayTreasure = []
def readData():
    global arrayTreasure
    try:
        file = open("C:/Users/u/Desktop/CS P4/2021/TreasureChestData.txt", "r")
        for i in range(5):
            quest = file.readline()
            ans = int(file.readline())
            points = int(file.readline())
            arrayTreasure.append(TreasureChest(quest,ans,points))
        file.close()
    except IOError:
        print("File doesn't exist")

#PROBLEM TO ADDRESS :
# arraytreasure biar [] so that dia boleh baca

#(c)(iv)
#main
readData()
quest = int(input(print("please choose question 1-5: ")))
Flag = False
Attempt = 0
while Flag == False:
    print("here's your question: ", arrayTreasure[quest-1].getQuestion())
    ans = int(input("Enter your answer: "))
    Flag = arrayTreasure[quest-1].checkAnswer(ans)
    Attempt = Attempt + 1
points= arrayTreasure[quest-1].getPoints(Attempt)
print("total points: ", points)
#knp - 1 = sbb append dia array [0,1,2,3,4] so kalau tak -1, user masukkan 1 dia akan baca array num 2

