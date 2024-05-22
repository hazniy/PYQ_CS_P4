#Q1
stackvowel = ['' for i in range(100)] #100 letters
stackconsonant = ['' for j in range(100)] #100 letters
voweltop = 0 #next free space stack vowel
consonanttop = 0 #next free space stack consonant

def PushData(letter):
    global voweltop, consonanttop
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        if voweltop == 100:
            print('stack vowel is full')
        else:
            stackvowel[voweltop] = letter
            voweltop = voweltop + 1
    else:
        if consonanttop == 100:
            print('stack consonant is full')
        else:
            stackconsonant[consonanttop] = letter
            consonanttop = consonanttop + 1

def ReadData():
    try:
        file = open('C:/Users/u/Desktop/StackData.txt','r')
        read = file.readline().strip()
        while read != '':
            PushData(read)
            read = file.readline().strip()
    except IOError:
        print('file doesnt exist')

def PopVowel():
    global voweltop
    if voweltop == 0:
        print('empty vowel stack')
    else:
        voweltop = voweltop - 1
        remove = stackvowel[voweltop]
        return remove

def PopConsonant():
    global consonanttop
    if consonanttop == 0:
        print('empty consonant stack')
    else:
        consonanttop = consonanttop - 1
        remove = stackconsonant[consonanttop]
        return remove

#main
ReadData()
print(stackconsonant)
print(stackvowel)
output = ''
for i in range(5):
    choice = input('please enter vowel or consonant: ').lower()
    if choice == 'vowel':
        remove = PopVowel()
        output = output + remove
    else:
        remove = PopConsonant()
        output = output + remove
print(output)

#Q2
def IterativeCalculate(num):
    tofind = num
    total = 0
    while num != 0:
        if tofind % num == 0:
            total = total + num
        num = num - 1
    return total
print(IterativeCalculate(10))

def RecursiveValue(num, tofind):
    if num == 0:
        return 0
    else:
        if tofind % num == 0:
            return num + RecursiveValue(num-1, tofind)
        else:
            return RecursiveValue(num-1, tofind)

print(RecursiveValue(50,50))

#Q3
import datetime
class Character:
    def __init__(self, charname, dob, intelligence, speed):
        self.charactername = charname #STRING
        self.dateofbirth = dob #DATE
        self.intelligence = intelligence #REAL
        self.speed = speed #INTEGER
    def getintelligence(self):
        return self.intelligence
    def getname(self):
        return self.charactername
    def setintelligence(self, newintel):
        self.intelligence = newintel
    def learn(self):
        self.intelligence = self.intelligence * 110/100
    def returnage(self):
        return 2023 - self.dateofbirth.year

FirstCharacter = Character('Royal', datetime.date(2019,1,1), 70, 30)
FirstCharacter.learn()
print('name', FirstCharacter.getname())
print('age', FirstCharacter.returnage())
print('intelligence', FirstCharacter.getintelligence())

class MagicCharacter(Character):
    def __init__(self, charname, dob, intelligence, speed, element):
        Character.__init__(self, charname, dob, intelligence, speed)
        self.element = element
    def learn(self):
        if self.element == 'fire' or self.element == 'water':
            self.intelligence = self.intelligence * 120 / 100
        elif self.element == 'earth':
            self.intelligence = self.intelligence * 130 / 100
        else:
            Character.learn(self)

FirstMagic = MagicCharacter('Light', datetime.date(2018,3,3), 75,22,'fire')
FirstMagic.learn()
print('name', FirstMagic.getname())
print('age', FirstMagic.returnage())
print('intelligence', FirstMagic.getintelligence())
