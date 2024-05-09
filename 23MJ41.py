#Q1 text file
DataArray = [0 for i in range(25)]
#main
DataFile = 'C:/Users/u/Desktop/Data.txt'
File = open(DataFile, 'r')
for i in range(25):
    read = int(File.readline())
    DataArray[i] = read
File.close()

def PrintArray(DataArray):
    for i in range(25):
        print(DataArray[i], " ", end=" ")
PrintArray(DataArray)

#problem to address
#why dia tak print one line <-- sbb string dia inc whitespace, if  //

def LinearSearch(DataArray, searchval):
    count = 0
    for i in range(25):
        if DataArray[i] == searchval:
            count = count + 1
    return count
#main
print('')
num = int(input('enter number between 0-100: '))
while num < 0 or num > 100:
    num = int(input('invalid range, please enter number between 0-100: '))
Count = LinearSearch(DataArray,num)
print('The number',num,'is found',Count,'times.')

#problem to address
#why dia tak output Count correctly? - because data type tadi string so dia tak output

#Q2 OOP
class Vehicle():
    def __init__(self,id,maxspeed,inc):
        self.__ID = id #STRING
        self.__MaxSpeed = maxspeed #INTEGER
        self.__CurrentSpeed = 0 #INTEGER
        self.__IncreaseAmount = inc #INTEGER
        self.__HorizontalPosition = 0 #INTEGER
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def SetCurrentSpeed(self, current):
        self.__CurrentSpeed = current
    def SetHorizontalPosition(self, hori):
        self.__HorizontalPosition = hori
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
            #updatedspeed = self.__CurrentSpeed + self.__IncreaseAmount
            #self.__HorizontalPosition = updatedspeed
    def OutputDetails(self):
        print('position',self.__HorizontalPosition)
        print('speed',self.__CurrentSpeed)

#PROBLEM TO ADDRESS
#knp ms buat currentspeed = maxspeed if its exceed the maxspeed, the ques just bagitau cant exceed?
#cuz cant exceed thats why dia assign new val which current speed to max

class Helicopter(Vehicle):
    def __init__(self, id, max, inc,verchange,maxheight):
        Vehicle.__init__(self, id, max, inc)
        self.__VerticalPosition = 0 #INTEGER
        self.__VerticalChange = verchange #INTEGER
        self.__MaxHeight = maxheight #INTEGER
    def GetVerticalPosition(self):
        return self.__VerticalPosition
    def IncreaseSpeed(self):
        def IncreaseSpeed(self):
            newVerticalPosition = self.__VerticalPosition + self.__VerticalChange
            if (newVerticalPosition <= self.__MaxHeight):  # if it has yet to exceed max height
                self.__VerticalPosition = newVerticalPosition  # use that value
            else:
                self.__VerticalPosition = self.__MaxHeight  # otherwise use max height

            newSpeed = Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self)  # override (getter)
            maxSpeed = Vehicle.GetMaxSpeed(self)
            if (newSpeed <= maxSpeed):
                Vehicle.SetCurrentSpeed(self, newSpeed)  # override (setter)
            else:
                Vehicle.SetCurrentSpeed(self, maxSpeed)

            newHorPos = Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self)
            Vehicle.SetHorizontalPosition(self, newHorPos)

        def OutputDetails(self):
            print("The horizontal position of the vehicle is:", Vehicle.GetHorizontalPosition(self))  # override
            print("The current speed of the vehicle is:", Vehicle.GetCurrentSpeed(self))  # override
            print("The vertical position of the vehicle is:", self.GetVerticalPosition())  # no need of override

car1 = Vehicle("Tiger", 100, 20)
heli1 = Helicopter("Lion", 350, 40, 3, 100)
car1.IncreaseSpeed()
car1.IncreaseSpeed()
car1.OutputDetails()

heli1.IncreaseSpeed()
heli1.IncreaseSpeed()
heli1.OutputDetails()

#PROBLEM TO ADDRESS
#why highlight output

#Q3 Stack
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
    if ColourTopPointer == 0 :
        return ''
    else:
        ReturnData = Animal[ColourTopPointer-1]
        ColourTopPointer = ColourTopPointer -1
        return ReturnData

def ReadData():
    AnimalFile = 'C:/Users/u/Desktop/AnimalData.txt'
    ColourFile = 'C:/Users/u/Desktop/ColourData.txt'
    try:
        File = open(AnimalFile, 'r')
        read = File.readline()
        while read != '':
            PushAnimal(read)
            File.readline()
        File.close()
        File2 = open(ColourFile, 'r')
        read2 = File2.readline()
        while read2 != '':
            PushColour(read2)
            File2.readline()
        File2.close()
    except IOError:
        print('file doesnt exist')
#PROBLEM TO ADDRESS
#how nak buat loop kat readline one by one if dia tak bagi range?

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
