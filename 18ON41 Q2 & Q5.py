#q2 ADT
def Hash(ISBN):
    val = (int(ISBN)/ 2000) + 1
    return val
#q5 OOP
class Cards():
    def __init__(self, Num, Shape):
        if (Num >= 0 and Num <= 9) and (Shape == 'Square' or Shape == 'Triangle' or Shape == 'Circle'):
            self.__Number = Num
            self.__Shape = Shape
        else:
            print('invalid Num or Shape')
    def GetNumber(self):
        return self.__Number
    def GetShape(self):
        return self.__Shape
#main
OneS = Cards(1,'Square')
def Compare(card1, card2):
    if card1.GetNumber() == card2.GetNumber() and card1.GetShape() == card2.GetShape():
        print('SNAP')
        return -1
    elif card1.GetNumber() > card2.GetNumber():
        return card1.GetNumber()
    else:
        return card2.GetNumber()
