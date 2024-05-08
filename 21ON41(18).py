#ques 1
def unknown(X,Y):
    if X < Y :
        print('sum of X and Y',X+Y)
        return (unknown(X+1,Y)*2)
    else:
        if X == Y:
            return 1
        else:
            print('sum of X and Y', X + Y)
            return (unknown(X-1,Y)/2)

#main
print(10,15)
unknown(10, 15)
print(10, 10)
unknown(10, 10)
print(15, 10)
unknown(15, 10)

def IterativeUnknown(X,Y):
    Total = 1
    while X != Y:
        print(X + Y)
        if X < Y:
            X = X + 1
            Total = Total * 2
        else:
            X = X - 1
            Total = int(Total / 2)
    return Total

print('10 & 15')
print(str(IterativeUnknown(10, 15)))
print('10 & 10')
print(str(IterativeUnknown(10, 10)))
print('15 & 10')
print(str(IterativeUnknown(15, 10)))

#ques 2
class Picture:
    def __init__(self, desc, width, height, col):
        self.description = desc #STRING
        self.width = width #INTEGER
        self.height = height #INTEGER
        self.framecolour = col #STRING
    def getdescription(self):
        return self.description
    def getheight(self):
        return self.height
    def getwidth(self):
        return self.width
    def getcolour(self):
        return self.framecolour
    def setdescription(self, newdesc):
        self.description = newdesc

array = [] #100 elements of picture

def readdata():
    count = 0
    try:
        file = open('C:/Users/u/Desktop/Pictures.txt','r')
        desc = file.readline().strip()
        while desc != '':
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            col = file.readline().strip()
            array.append(Picture(desc,width,height,col))
            count = count + 1
            desc = file.readline().strip()
        file.close()
    except IOError:
        print('file doesnt exist')
    return count

#better count letak luar and return count sebaris dgn try and except
#main
count = readdata()
print('there are',count,'picture in the array')
col = input('enter frame colour: ').lower()
width = int(input('enter maximum width: '))
height = int(input('enter maximum height: '))
for i in range(len(array)):
    if array[i].framecolour.lower() == col :
        if array[i].width <= width:
            if array[i].height <= height:
                print('description: ', array[i].getdescription())
                print('witdh: ',array[i].getwidth())
                print('height: ', array[i].getheight())
#if nak print array kena guna getter (thats the whole purpose of getter lol)
#ques 3 binary tree
#(a)
ArrayNodes = [[0 for i in range(3)]for j in range(20)] #ARRAY OF INTEGER
RootPointer = -1 #INTEGER #points first node in the binary tree
FreeNode = 0 #INTEGER #points first empty node in array
#(b)
def AddNode():
    global ArrayNodes,RootPointer,FreeNode
    NodeData = int(input('Enter the data: '))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        #dia masukkan dulu dlm first empty slot
        if RootPointer == -1:
            RootPointer = 0
            #maksudnya list tak empty dh, thats why jadi 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]: #compare data
                    if ArrayNodes[CurrentNode][0] == -1: #check leftpointer empty ke tak
                        ArrayNodes[CurrentNode][0] = FreeNode #masuk leftpointer
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0] #dia akan compare dgn leftpointer next stage
                else:
                    if ArrayNodes[CurrentNode][2] == -1: #check rightpointer
                        ArrayNodes[CurrentNode][2] = FreeNode #masuk righpinter
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print('Tree is full')
#(c)
def PrintAll():
    global ArrayNodes
    for i in range(20):
        LeftPointer = ArrayNodes[i][0]
        Data = ArrayNodes[i][1]
        RightPointer = ArrayNodes[i][2]
        print(LeftPointer, '', Data, '',RightPointer)

#(d)(i)
#main
for i in range(10):
    AddNode()
PrintAll()

#(e)(i)
def InOrder(Root):
    if ArrayNodes[Root][0] != -1:
        InOrder((ArrayNodes[Root][0]))
    print(ArrayNodes[Root][1])
    if ArrayNodes[Root][2] != -1:
        InOrder(ArrayNodes[Root][2])
InOrder(RootPointer)
