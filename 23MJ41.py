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
