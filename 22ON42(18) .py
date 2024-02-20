#ques 1 text file
#(a)
DataArray = [0 for i in range(100)]
#(b)
def ReadFile():
    global DataArray
    try:
        file = open('C:\ Users\ u\Desktop\CS P4\9618_w22_sf_41.zip\11_9618_41_Confidential Source Files November 2022\IntegerData.txt', 'r')
        for i in range(100):
            read = file.readline()
            DataArray[i] = int(read)
        file.close()
    except IOError:
        print('file doesnt exist')
#(c)
def FindValues():
    global DataArray
    count = 0
    num = -1
    while num < 1 or num > 100:
     num = int(input(print('please enter a valid num: ')))
    for i in range(100):
        if num == DataArray[i]:
            count = count + 1
    return count
#(d)(i)
ReadFile()
Return = FindValues()
print('the number was found', str(Return), 'times')
#(e)
def BubbleSort(DataArray):
    upperB = 99
    lowerB = 0
    top = upperB
    swap = True
    while swap == True or top !=0:
        for i in range(lowerB, top-1):
            if DataArray[i] > DataArray[i+1]:
                temp = DataArray[i]
                DataArray[i] = DataArray[i+1]
                DataArray[i+1] = temp
                swap = False
        top = top - 1
print(BubbleSort(DataArray))
