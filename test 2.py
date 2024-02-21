StudentArray = [['']*2 for i in range(11)] #String
def ReadStudentMark():
    try:
        file = open('C:/Users/N129ALS22030/Downloads/StudentMark.txt','r' )
        for i in range(11):
            StudentArray[i][0] = file.readline()
            StudentArray[i][1] = file.readline()
        file.close()
    except IOError:
        print('file doesnt exist')
def OutputStudentMarks():
    for i in range(11):
        StudentName = StudentArray[i][0]
        Mark = StudentArray[i][1]
        print(StudentName, Mark, end='')

def newlist(name, mark):
    top = 11
    flag = True
    while flag == True or top != 0:
        for i in range(top-1):
            if mark > StudentArray[i][1]:
                temp = mark
                temp2 = name
                mark = StudentArray[i + 1][1]
                name = StudentArray[i+1][0]
                StudentArray[i + 1][1] = temp
                StudentArray[i + 1][0] = temp2
                flag = False
        top = top - 1
#main
ReadStudentMark()
OutputStudentMarks()
name = ''
while len(name) != 4:
    name = input(print('please enter your name: '))
mark = 0
while mark < 1 or mark > 100:
    mark = int(input(print('please enter your mark: ')))
newlist(name, mark)

def WriteTopStudent():
    filename = 'NewStudentMark.txt'
    file = open(filename, 'w')
    for i in range(10):
        name = StudentArray[i][0]
        mark = StudentArray[i][1]
        file.writelines(name)
        file.writelines(mark)
    file.close()
