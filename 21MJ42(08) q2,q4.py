#ques 2 hashing
def Hash(BookingID):
    HashV = BookingID % 100000 + 3 #mod
    return HashV
#ques 3 OOP
class QuizClass():
    def __init__(self):
        self.__NumberOfQuestions = 0
        self.__Questions = []
    def AddQuestion(self, QuestionObject):
        if self.__NumberOfQuestions < 20:
            self.__Questions[self.__NumberOfQuestions] = QuestionObject
            self.__NumberOfQuestions = self.__NumberOfQuestions + 1
            return True
        else:
            return False


FirstQuiz = QuizClass()
Question1 = QuestionClass("What is 100/5?", "20", 1)
FirstQuiz.AddQuestion(Question1)
