#ques 5 OOP
class Lesson():
    def __init__(self,type,instructor):
        self.LessonType = type #STRING
        self.Instructor = instructor #STRING
    def GetLessonType(self):
        return self.LessonType
    def GetInstructor(self):
        return self.Instructor
    def SetLessonType(self,l):
        self.LessonType = l
    def SetInstructor(self, i):
        self.Instructor = i
def GetFee(level):
    if level == 'B':
        fee = 45
    elif level == 'I':
        fee = 50
    elif level == 'A':
        fee = 55
    else:
        fee = -1
    return fee
LessonArray = []
type = 'Improve Your Serve'
instructor = 'David'
LessonArray[2] = Lesson(type,instructor)
