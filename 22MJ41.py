#Ques 1 text file
#(a)
TopPlayerArray = [['']*2 for i in range(11)] #STRING
#(b)
def ReadHighScores():
    try:
        file = open('C:/Users/u/Desktop/HighScore.txt', 'r')
        for i in range(11):
            readplayer = file.readline()
            readscore = file.readline()
            TopPlayerArray[i][0] = readplayer
            TopPlayerArray[i][1] = readscore
        file.close()
    except IOError:
        print('file doesnt exist')
#(c)
def OutputHighScores():
    for i in range(11):
        player = TopPlayerArray[i][0].strip()
        Score = TopPlayerArray[i][1]
        print(player,'', Score, end='')
    print('')
#PROBLEM TO ADDRESS
#dia tak output one line <-- letak strip()
#(d)(i)
#main
ReadHighScores()
OutputHighScores()
#(e)(i)
player = input('enter ur name: ')
while len(player) != 3:
    player = input('invalid name, please enter again: ')
score = int(input('enter ur score: '))
while score < 1 or score > 10000:
    score = int(input('invalid score, please enter again: '))
#(ii)
def newtopten(player, score):
    flag = False
    n = 11
    while flag == False or n>0:
        TopPlayerArray[10][1] = score
        for i in range(11):
            data = TopPlayerArray[i][1]
            if int(score) > int(data):
                tempplayer = TopPlayerArray[i][0]
                TopPlayerArray[i][0] = player
                player = tempplayer

                tempscore = TopPlayerArray[i][1]
                TopPlayerArray[i][1] = score
                score = tempscore
                flag = True
        n = n -1
#(iii)
ReadHighScores()
print('before insert new player')
OutputHighScores()
player = input('enter ur name: ')
while len(player) != 3:
    player = input('invalid name, please enter again: ')
score = int(input('enter ur score: '))
while score < 1 or score > 10000:
    score = int(input('invalid score, please enter again: '))
newtopten(player, score)
print('after insert new player')
OutputHighScores()

def WriteTopTen():
    file = open('NewHighScore.txt', 'w')
    for i in range(11):
        player = TopPlayerArray[i][0]
        score = TopPlayerArray[i][1]
        file.write(player)
        file.write(score)
    file.close()

###### q2 ######
class Balloon():
    def __init__(self, item, col):
        self.__Health = 100 #INTEGER
        self.__Colour = col #STRING
        self.__DefenceItem = item #STRING
    def ChangeHealth(self, change):
        self.__Health = self.__Health + change
    def GetDefenceItem(self):
        return self.__DefenceItem
    def CheckHealth(self):
        if self.__Health <= 0:
            print('no health remaining')
            return True
        else:
            print('health remaining', self.__Health)
            return False

def defend(Balloon1):
    healthoppo = int(input('enter the health of opponent: '))
    Balloon1.ChangeHealth(-healthoppo)
    print('your defence item: ', item)
    data = Balloon1.CheckHealth()
    return Balloon1

#main
item = input('insert your defence item: ')
col = input('insert the colour of the balloon: ')
Balloon1 = Balloon(item,col)
defend(Balloon1)


#####q3#####
QueueArray = ['' for x in range(10)] #ARRAY OF STRING
head = 0 #INTEGER
tail = 0 #INTEGER
numitem = 0 #INTEGER

def enqueue(DataToAdd): #RETURNS BOOLEAN
    global QueueArray,head,tail,numitem
    if numitem == 10:
        return False
    QueueArray[tail] = DataToAdd
    if tail >= 9:
        tail = 0
    else:
        tail = tail + 1
    numitem = numitem + 1
    return True

def dequeue(): #RETURNS BOOLEAN
    global QueueArray, head, tail, numitem
    if numitem == 0:
        return False
    else:
        remove = QueueArray[head]
        if head >= 9:
            head = 0
        else:
            head = head + 1
        numitem = numitem - 1
        print('data remove',remove)
        return QueueArray[head+1]

#main
for x in range(11):
    data = input('enter your data: ')
    Return = enqueue(data)
    if Return == True:
        print('success added')
    else:
        print('not success, queue is full')
val = dequeue()
print(val)
val2 = dequeue()
print(val2)

