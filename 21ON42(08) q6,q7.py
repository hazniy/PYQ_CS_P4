#ques 6 stack
#(a) most recent
#(b)(i)
def additemtostack (errorarray, lastitem, error1):
    if lastitem == 99:
        return False
    else:
        errorarray[lastitem+1] = error1
        lastitem = lastitem+1
        return True
#(ii) byref byval
#BYVALUE stops the value being changed outside the function but BYREF changes the value where called from
#The function needs to change the values in ErrorArray and/or LastItem in main/where called
#otherwise they would not be changed outside of the function
#Error1's value does not change in the function // no changes to Error1's value need reflecting where it was called /to the original
#(iii)
def removeitem (errorarray, lastitem):
    global nullerror
    if lastitem == -1 :
        return nullerror
    else:
        itemremove = errorarray[lastitem]
        lastitem = lastitem - 1
        return itemremove
#(iv)
enqueue = ['' for i in range(100)]
def runerror (errorcomplete, errorarray):
    global nullerror
    dataitem = removeitem(errorarray,lastitem=1)
    if dataitem == nullerror:
        print('stack empty')
    else:
        if enqueue[dataitem] == True:
            print('item added to queue')
        else:
            print('item not added to queue')
#ques 7 OOP
class Box:
    def __init__(self, Sizep, FirstContent, LockNumber):
        self.__Size = Sizep #string
        self.__Lock = LockNumber #string
        self.__Strength = 100 #integer
        self.__Contents = [] #array 10 elements of FieldObject
        self.__Contents.append(FirstContent)
    def unlock(self, Key):
        if self.__Lock == Key:
            return True
        else:
            self.__Strength = self.__Strength - 1
        if self.__Strength <= 0:
            return True
        else:
            return False

def LoadGame():
    Filename = "progress.txt"
    try:
        F = open(Filename, "r")
        GameData = F.read()
        F.close()
    except:
        print("File not found")
