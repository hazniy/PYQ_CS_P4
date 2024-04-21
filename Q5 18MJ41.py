#ques 5 OOP
class GameElement:
    def __init__(self, posiX, posiY, width, height, imgfilename):
        self.posiX = posiX
        self.posiY = posiY
        self.width = width
        self.filename = imgfilename
    def ReturnDetails(self):
        return self.posiX, self.posiY, self.width, self.filename

class Scenery(GameElement):
    def __init__(self, posiX, posiY, width, height, imgfilename, Cause, DPoints):
        GameElement.__init__(self, posiX, posiY, width, height, imgfilename) #no : after this
        self.CauseDamage = Cause
        self.DamagePoints = DPoints
    def GiveDamagePoins(self):
        if self.CauseDamage == True:
            return self.DamagePoints
        else:
            return 0
    def GetScenery(self):
        return self.CauseDamage, self.DamagePoints

GiftBox = Scenery(150,150,50,75,'box.png',True,50)
