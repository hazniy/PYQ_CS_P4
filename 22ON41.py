#ques 1 text file
#(a)
DataArray = [] #integer

def ReadFile():
    file = open('C:/Users/N129ALS22030/Desktop/IntegerData.txt','r')
    try:
        for i in range(100):
            read = file.readline().strip()
            DataArray.append(read)
        file.close()
    except IOError:
        print('file doesnt exist')

def FindValues():
    val = 0
    count = 0
    while val < 1 or val > 100:
        val = int(input('enter a number to search: '))
    for i in range(100):
        if DataArray[i] == str(val):
            count = count + 1
    return count

#main
ReadFile()
data = FindValues()
if data == 0:
    print('the number doesnt exist in the array sorry')
else:
    print('the number occur',data,'times')

#(e)
def BubbleSort(DataArray):
    upperB = 99
    lowerB = 0
    top = upperB
    swap = True
    while swap == True or top !=0:
        for i in range(lowerB, top-1):
            if DataArray[i] > DataArray[i+1]:
                temp = DataArray[i]
                DataArray[i] = DataArray[i+1]
                DataArray[i+1] = temp
                swap = False
        top = top - 1
print(BubbleSort(DataArray))


#ques 2 OOP
#(a)(i)
class Card:
    def __init__(self, Num, Col):
        self.__Number = Num
        self.__Colour = Col
#(a)(ii)
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
#(a)(iii)
OneRed = Card(1, 'red')
TwoRed = Card(2, 'red')
ThreeRed = Card(3, 'red')
FourRed = Card(4, 'red')
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")
#(b)(i)
class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5
#(b)(ii)
    def GetCard(self, Position):
        return self.__Cards[Position]
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)

#(c)(i)
def CalculateValue(Player):
    Score = 0
    for i in range(0, 4):
        CardGot = Player.GetCard(i)
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColour()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score
#(c)(ii)
Player1score = CalculateValue(Player1)
Player2score = CalculateValue(Player2)
if Player1score > Player2score:
     print("Player 1 wins")
elif Player1score < Player2score:
     print("Player 2 wins")
else:
     print("It's a draw")

#ques 3 binary tree
ArrayNodes = [[-1 for i in range(3)]for j in range(20)]
print(ArrayNodes)

freenodes = 6
rootpointer = 0
ArrayNodes[0][0] = 1
ArrayNodes[0][1] = 20
ArrayNodes[0][2] = 5
ArrayNodes[1][0] = 2
ArrayNodes[1][1] = 15
ArrayNodes[2][1] = 3
ArrayNodes[2][2] = 3
ArrayNodes[3][1] = 9
ArrayNodes[3][2] = 4
ArrayNodes[4][1] = 10
ArrayNodes[5][1] = 58
print(ArrayNodes)

def SearchValue(root,valfind):
    if root == -1:
        return -1
    else:
        if ArrayNodes[root][1] == valfind:
            return root
        else:
            if ArrayNodes[root][1] == -1:
                return -1
    if ArrayNodes[root][1] > valfind:
        return SearchValue(ArrayNodes[root][0], valfind)
    if ArrayNodes[root][1] < valfind:
        return SearchValue(ArrayNodes[root][2], valfind)

def PostOrder():

#main
data = SearchValue(0,15)
if data == -1:
    print('not found')
else:
    print(data)
PostOrder()
