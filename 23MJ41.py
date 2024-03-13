DataArray = ['' for i in range(25)]
#main
DataFile = 'C:/Users/N129ALS22030/Desktop/Data.txt'
File = open(DataFile, 'r')
for i in range(25):
    read = File.readline()
    DataArray[i] = read
File.close()
def PrintArray(DataArray):
    data = ''
    for i in range(25):
        data = data + DataArray[i]
    print(data)
PrintArray(DataArray)
def LinearSearch(DataArray, searchval):
    count = 0
    for i in range(25):
        if DataArray[i] == searchval:
            count = count + 1
    return count
#main
num = int(input('enter number between 0-100: '))
while num < 0 or num > 100:
    num = int(input('invalid range, please enter number between 0-100: '))
Count = LinearSearch(DataArray,num)
print('The number',num,'is found',Count,'times.')

Animal = ['' for i in range (20)]
Colour = ['' for j in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0
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
    if AnimalTopPointer == 0 :
        return ''
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer = AnimalTopPointer -1
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
    if ColourTopPointer == 0 :
        return ''
    else:
        ReturnData = Animal[ColourTopPointer-1]
        ColourTopPointer = ColourTopPointer -1
        return ReturnData

def ReadData():
    AnimalFile = 'C:/Users/N129ALS22030/Desktop/AnimalData.txt'
    ColourFile = 'C:/Users/N129ALS22030/Desktop/ColourData.txt'
    try:
        File = open(AnimalFile, 'r')
        File2 = open(ColourFile, 'r')
        read = File.readline()
        read2 = File2.readline()
        PushAnimal(read)
        PushColour(read2)
        File.close()
        File2.close()
    except IOError:
        print('file doesnt exist')

def OutputItem():
    Col = PopColour()
    animal = PopAnimal()
    if Col != '' and animal != '':
        print(Col + animal)
    elif Col == '':
        PushAnimal(animal)
        print('no colour')
    elif animal == '':
        PushColour(Col)
        print('no animal')

#main
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
class Vehicle():
    def __init__(self,id,maxspeed,current,inc,hori):
        self.__ID = id #STRING
        self.__MaxSpeed = maxspeed #INTEGER
        self.__CurrentSpeed = current #INTEGER
        self.__IncreaseAmount = inc #INTEGER
        self.__HorizontalPosition = hori #INTEGER
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreasseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def SetCurrentSpeed(self, newcurrent):
        self.__CurrentSpeed = newcurrent
    def SetHorizontalPosition(self, newhori):
        self.__HorizontalPosition = newhori
    def IncreaseSpeed(self):
        if self.__CurrentSpeed <= self.__MaxSpeed:
            updatedspeed = self.__CurrentSpeed + self.__IncreaseAmount
            self.__HorizontalPosition = updatedspeed

class Helicopter(Vehicle):
    def __init__(self,id,max,current,inc,hori,verposi,verchange,maxheight):
        Vehicle.__init__(self,id,max,current,inc,hori)
        self.__VerticalPosition = verposi #INTEGER
        self.__VerticalChange = verchange #INTEGER
        self.__MaxHeight = maxheight #INTEGER
    def GetVerticalPosition(self):
        return self.__VerticalPosition
    def IncreaseSpeed(self):
        Helicopter.GetVerticalPosition(self)
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition <= self.__MaxHeight:
            if Helicopter.GetCurrentSpeed(self) <= Helicopter.GetMaxSpeed(self):
                updatedspeed = self.__CurrentSpeed + self.__IncreaseAmount
                Helicopter.SetHorizontalPosition(self,updatedspeed)
def output():
    vehicle = Vehicle('',0,0,0,0)
    print(Vehicle.GetHorizontalPosition(vehicle))
    print(Vehicle.IncreaseSpeed(vehicle))
    if vehicle == 'Helicopter':
        print(Helicopter.GetVerticalPosition(vehicle))
#main
car = Vehicle('Tiger',100,0,20,0)
heli = Helicopter('Lion', 350, 0, 40, 0, 0, 3, 100)

