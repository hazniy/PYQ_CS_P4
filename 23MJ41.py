#Q1
DataArray = [] #25 integer
try:
    file = open('C:/Users/u/Desktop/Data.txt','r')
    read = file.readline().strip()
    while read != '':
        DataArray.append(read)
        read = file.readline().strip()
except IOError:
    print('file doesnt exist')
print(DataArray)

def PrintArray(DataArray):
    text = ''
    for i in range(len(DataArray)):
        text = text + ' ' + DataArray[i]
    print(text)
PrintArray(DataArray)

def LinearSearch(DataArray, searchval):
    count = 0
    for i in range(len(DataArray)):
        if searchval == int(DataArray[i]):
            count = count + 1
    return count

#main
searchval = int(input('enter num between 0-100: '))
while searchval < 0 or searchval > 100:
    searchval = int(input('number out of range, please enter new number: '))
count = LinearSearch(DataArray,searchval)
print('the number',searchval,'is found', count,'times')

#Q2
class vehicle:
    def __init__(self, id, maxspeed, incamn):
        self.id = id #STRING
        self.maxspeed = maxspeed #INTEGER
        self.increaseamount = incamn #INTEGER
        self.currentspeed = 0 #INTEGER
        self.horizontalposition = 0 #INTEGER
    def getcurrentspeed(self):
        return self.currentspeed
    def getincreaseamount(self):
        return self.increaseamount
    def gethorizontalposition(self):
        return self.horizontalposition
    def getmaxspeed(self):
        return self.maxspeed
    def setcurrentspeed(self, curspeed):
        self.currentspeed = curspeed
    def sethorizontalposition(self, horiposi):
        self.horizontalposition = horiposi
    def increasespeed(self):
        self.currentspeed = self.currentspeed + self.increaseamount
        if self.currentspeed <= self.maxspeed:
            self.horizontalposition = self.horizontalposition + self.currentspeed
        else:
            self.currentspeed = self.maxspeed
            self.horizontalposition = self.currentspeed
    def outputcurrentpoosition(self):
        print('horizontal position', self.horizontalposition)
        print('current speed', self.currentspeed)

class helicopter(vehicle):
    def __init__(self, id, maxspeed, incamn, vertchange, maxheight):
        vehicle.__init__(self, id, maxspeed, incamn)
        self.verticalposition = 0 #INTEGGER
        self.verticalchange = vertchange #INTEGER
        self.maxheight = maxheight #INTEGER
    def getverticalposition(self):
        return self.verticalposition
    def increasespeed(self):
        self.verticalposition = self.verticalposition + self.verticalchange
        if self.verticalposition > self.maxheight:
            self.verticalposition = self.maxheight #knp dia tak guna self.maxheight = maxheight
        vehicle.setcurrentspeed(self, vehicle.getcurrentspeed(self) + vehicle.getincreaseamount(self))
        if vehicle.getcurrentspeed(self) > vehicle.getmaxspeed(self):
            vehicle.setcurrentspeed(self, vehicle.getmaxspeed(self))
        vehicle.sethorizontalposition(self, vehicle.gethorizontalposition(self)+vehicle.getcurrentspeed(self))
    def outputcurrentpoosition(self):
        print('horizontal position', vehicle.gethorizontalposition(self))
        print('current speed', vehicle.getcurrentspeed(self))
        print('vertical position', self.verticalposition)

car = vehicle('Tiger', 100, 20)
car.increasespeed()
car.increasespeed()
car.outputcurrentpoosition()
print('')
heli = helicopter('Lion', 350, 40, 3, 100)
heli.increasespeed()
heli.increasespeed()
heli.outputcurrentpoosition()

#Q3
Animal = ['' for i in range(20)] #20 animals
#kalau kita ada index/pointer, kena assign available slot dulu thats why takleh guna append
Colour = ['' for j in range(10)] #10 colours
AnimalTopPointer = 0 #point next free space animal
ColourTopPointer =  0 #point next free space colour

def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ''
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ''
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

def ReadData():
        try:
            fileanimal = open('C:/Users/u/Desktop/AnimalData.txt', 'r')
            filecolour = open('C:/Users/u/Desktop/ColourData.txt', 'r')
            readanimal = fileanimal.readline().strip()
            readcolour = filecolour.readline().strip()
            while readanimal != '':
                PushAnimal(readanimal)
                readanimal = fileanimal.readline().strip()
            fileanimal.close()
            while readcolour != '':
                PushColour(readcolour)
                readcolour = filecolour.readline().strip()
            filecolour.close()
        except IOError:
            print('file doesnt exist')

def OutputItem():
    thisanimal = PopAnimal()
    thiscolour = PopColour()
    if thiscolour == '':
        PushAnimal(thisanimal)
        print('no colour')
    elif thisanimal == '':
        PushColour(thiscolour)
        print('no animal')
    else:
        print(thiscolour, thisanimal)

#main
ReadData()
print(Animal)
print(Colour)
OutputItem()
OutputItem()
OutputItem()
OutputItem()
print(Animal)
print(Colour)
