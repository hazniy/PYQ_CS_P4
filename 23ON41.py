#Q1
def iterativevowels(value):
    total = 0
    lengthstring = len(value)
    for x in range(lengthstring):
        firstchar = value[0].lower()
        if firstchar == 'a' or firstchar == 'e' or firstchar == 'i' or firstchar == 'o' or firstchar == 'u':
            total = total + 1
        value = value[1:lengthstring]
    return total
print(iterativevowels('house'))

def recursivevowel(value):
    if len(value) == 0:
        return 0
    else:
        firstchar = value[0].lower()
    if firstchar == 'a' or firstchar == 'e' or firstchar == 'i' or firstchar == 'o' or firstchar == 'u':
        return 1 + recursivevowel(value[1:len(value)])
    else:
        return recursivevowel(value[1:len(value)])
#takyah total dh, return 1 + recursive lagi skali
print(recursivevowel('imagine'))

#print one part only
value = 'hai'
print(value[0]) #first char
print(value[0:3]) #first until what

#Q2
queue = [] #ID STRING
headpointer = -1 #point first element
tailpointer = 0 #next available space

def enqueue(value):
    global tailpointer, headpointer
    if tailpointer == 50: #not > cuz 0-49
        print('queue is full')
    else:
        queue.append(value)
        tailpointer = tailpointer + 1
        if headpointer == -1:
            headpointer = 0

def dequeue():
    global headpointer, tailpointer
    if headpointer == -1 or headpointer == tailpointer:
        print('queue empty')
        return 'empty'
    else:
        headpointer = headpointer + 1
        return queue[headpointer-1]

def readdata():
    try:
        file = open('C:/Users/u/Desktop/QueueData.txt', 'r')
        read = file.readline().strip()
        while read != '':
            enqueue(read)
            read = file.readline().strip()
        file.close()
    except IOError:
        print('file doesnt exist')

class recorddata:
    def __init__(self, id, total):
        self.id = id #string
        self.total = total #integer
    def getid(self):
        return self.id
    def gettotal(self):
        return self.total
    def settotal(self, total):
        self.total = total
    def setid(self, id):
        self.id = id
record = [] #store 50 items recorddata
numrecord = 0 #store total num in array

def totaldata():
    global numrecord, record
    dataaccessed = dequeue()
    flag = False
    if numrecord == 0:
        record.append(recorddata(dataaccessed,1))
        numrecord = numrecord + 1
        flag = True
    else:
        for x in range(numrecord):
            if record[x].getid() == dataaccessed:
                record[x].settotal(record[x].gettotal() + 1)
                flag = True
    if flag == False:
        record.append(recorddata(dataaccessed,1))
        numrecord = numrecord + 1

def outputrecord():
    for X in range(numrecord):
        print("ID", record[X].getid(), " Total ", record[X].gettotal())

#main
readdata()
while headpointer != tailpointer:
    totaldata()
outputrecord()

#Q3
class Character:
    def __init__(self, name, xposi, yposi):
        self.name = name #string
        self.xposition = xposi #integer
        self.yposition = yposi #integer
    def getxposition(self):
        return self.xposition
    def getyposition(self):
        return self.yposition
    def setxposition(self, newxposi):
        if newxposi > 1000:
            self.xposition = 1000
        elif newxposi < 0:
            self.xposition = 0
        else:
            self.xposition = newxposi
    def setyposition(self, newyposi):
        if newyposi > 1000:
            self.yposition = 1000
        elif newyposi < 0:
            self.yposition = 0
        else:
            self.yposition = newyposi
    def move(self, move):
        if move.lower() == 'up':
            self.yposition = self.yposition + 10
        elif move.lower() == 'down':
            self.yposition = self.yposition - 10
        elif move.lower() == 'left':
            self.xposition = self.xposition - 10
        elif move.lower() == 'right':
            self.xposition = self.xposition + 10
        else:
            print('move not valid')

Jack = Character('Jack', 50, 50)

class BikeCharacter(Character):
    def __init__(self, name, xposi, yposi):
        Character.__init__(self, name, xposi, yposi)
    def move(self, move):
        if move.lower() == 'up':
            self.yposition = self.yposition + 20
        elif move.lower() == 'down':
            self.yposition = self.yposition - 20
        elif move.lower() == 'left':
            self.xposition = self.xposition - 20
        elif move.lower() == 'right':
            self.xposition = self.xposition + 20
        else:
            print('move not valid')

Karla = BikeCharacter('Karla', 100, 50)

character = 'Hazni'
while character != 'Karla' and character != 'Jack':
    character = input('enter name of the character: ')
move = 'centre'
while move.lower() != 'up' and move.lower() != 'down' and move.lower() != 'left' and move.lower() != 'right':
    move = input('enter which direction you want to move: ')
if character == 'Jack':
    Jack.move(move)
    Jack.setxposition(Jack.getxposition())
    Jack.setyposition(Jack.getyposition())
    print('Jack new position is X =',Jack.getxposition(),'Y =',Jack.getyposition())
else:
    Karla.move(move)
    Karla.setxposition(Karla.getxposition())
    Karla.setyposition(Karla.getyposition())
    print('Karla new position is X =', Karla.getxposition(), 'Y =', Karla.getyposition())
