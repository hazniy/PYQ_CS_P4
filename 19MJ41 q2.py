#ques 2 OOP, sorting
class Player:
    def __init__(self,playerID):
        self.Score = 0
        self.Category = 'Not Qualified'
        self.PlayerID = playerID

    def SetScore(self, ScoreInput):
        if ScoreInput >= 0 and ScoreInput <= 150:
            self.Score = ScoreInput
            return True
        else:
            print('score is invalid')
            return False

    def SetCategory(self):
        if self.Score > 120:
            self.Category = 'Advanced'
        elif self.Score > 80 and self.Score <= 120:
            self.Category = 'Intermediate'
        elif self.Score >= 50 and self.Score <= 80:
            self.Category = 'Beginner'
        else:
            self.Category = 'Not Qualified'

    def SetPlayerID(self):
        newPlayerID = input('enter a new player ID: ')
        while len(newPlayerID) > 15 and len(newPlayerID) < 4:
            newPlayerID = input('enter new value: ')
        self.PlayerID = newPlayerID

    def GetScore(self):
        return self.Score
    def GetCategory(self):
        return self.Category
    def GetPlayerID(self):
        return self.PlayerID

def CreatePlayer():
    playerID = input('enter a player ID: ')
    score = int(input('enter a score: '))
    JoannePlayer = Player(playerID)
    if JoannePlayer.SetScore(score) == False:
        print('invalid score')
    else:
        JoannePlayer.SetCategory()
        print(JoannePlayer.GetCategory())
