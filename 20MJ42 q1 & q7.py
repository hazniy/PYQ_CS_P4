#ques 1 file txt
try:
 file = open('MyData.txt')
except:
 print ("No file found")

#ques 7 OOP
import random
class Character:
 def __init__(self, name):
  self.Name = name
  self.skill = 0
  self.health = 50
  self.shield = random.randint(1,25)
 def GetSkill(self) :
  return self.skill

 def SetSkill(self, Value):
  if Value < 10 or Value > 25:
   return -1
  else:
    if self.skill + Value >= 200:
     skill = 200
     return 0
    else:
      self.skill = self.skill + Value
      return 1

CharacterArray = []
CharacterArray[0] = Character("Victory")
