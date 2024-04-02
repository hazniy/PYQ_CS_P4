class Card():
    def __init__(self,num,col):
        self._Number = num #integer
        self._Colour = col #string
    def GetNumber(self):
        return self._Number
    def GetColour(self):
        return self._Colour

#main
Card1 = Card(1,'red')
Card2 = Card(2,'red')
Card3 = Card(3,'red')
Card4 = Card(4,'red')
Card5 = Card(5,'red')

Card6 = Card(1,'blue')
Card7 = Card(2,'blue')
Card8 = Card(3,'blue')
Card10 = Card(4,'blue')
Card11 = Card(5,'blue')

Card12 = Card(1,'yellow')
Card13 = Card(2,'yellow')
Card14 = Card(3,'yellow')
Card15 = Card(4,'yellow')
Card16 = Card(5,'yellow')

class Hand():
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self._Cards = [Card] #array of integer
        self._Cards.append(Card1)
        self._Cards.append(Card2)
        self._Cards.append(Card3)
        self._Cards.append(Card4)
        self._Cards.append(Card5)
        self._firstcard = 0 #integer
        self._NumberCards = 5 #integer
    def GetCard(self, index):
        return self._Cards[index]

def CalculateValue(player):
    for i in range(9):
        if player.GetColour[i] == 'red':
            player.Number = player.Number + 5
        elif player.GetColour[i] == 'blue':
            player.Number = player.Number + 10
        elif player.GetColour[i] == 'yellow':
            player.Number = player.Number + 15
    return player.GetNumber

player1 = Hand(Card1,Card2,Card3,Card4,Card12)
player2 = Hand(Card13,Card14,Card15,Card16,Card6)
data1 = CalculateValue(player1)
data2 =  CalculateValue(player2)
if data1 > data2:
    print('player 1 is the winner')
elif data1 < data2:
    print('player 2 is the winner')
else:
    print('draw')
