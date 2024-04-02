DataArray = [] #integer

def ReadFile():
    file = open('C:/Users/N129ALS22030/Desktop/IntegerData.txt','r')
    try:
        for i in range(100):
            read = file.readline().strip()
            DataArray.append(read)
        file.close()
    except IOError:
        print('file doesnt exist')

def FindValues():
    val = 0
    count = 0
    while val < 1 or val > 100:
        val = int(input('enter a number to search: '))
    for i in range(100):
        if DataArray[i] == str(val):
            count = count + 1
    return count

#main
ReadFile()
data = FindValues()
if data == 0:
    print('the number doesnt exist in the array sorry')
else:
    print('the number occur',data,'times')

def BubbleSort(DataArray):
    flag = False
    while flag == False:
        for i in range(len(DataArray)-1):
            if DataArray[i] > DataArray[i+1]:
                temp = DataArray[i]
                DataArray[i] = DataArray[i+1]
                DataArray[i+1] = temp
                flag = False
    print(DataArray)
BubbleSort(DataArray)

