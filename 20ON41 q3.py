#ques 3 OOP
class PuzzlePLayer:
    def __init__(self):
        self.PlayerID = 'PL12a3'
        self.Name = ''
        self.Score = 0
    def getplayerid(self):
        return self.PlayerID
    def getscore(self):
        return self.Score
    def Name(self):
        return self.Name
    def setplayerid(self,id):
        if len(id) == 6 and id[0:2].upper() == 'PL':
                self.PlayerID = id
                return True
        else:
            return False
