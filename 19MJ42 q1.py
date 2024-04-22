#ques 1 OOP
#(b)
class ExaminationPaper():
    def __init__(self, centrenum, candnum):
        self.FinalMark = 0
        self.Grade = 'Fail'
        self.PaperID = centrenum + candnum
    def SetFinalMark(self, mark):
        if mark >= 0 and mark <= 90:
            self.FinalMark = mark
            return True
        else:
            return False
    def SetGrade(self, mark, DistMark, MeritMark, PassMark):
        if mark >= DistMark:
            self.Grade = 'Distinction'
        elif mark >= MeritMark:
            self.Grade = 'Merit'
        elif mark >= PassMark:
            self.Grade = 'Pass'
        else:
            self.Grade = 'Fail'
    def GetFinalMark(self):
        return self.FinalMark
    def GetGrade(self):
        return self.Grade
    def GetPaperID(self):
        return self.PaperID
#main
def Main():
    centrenum = input('enter centre number: ')
    candnum = input('enter a candidate number: ')
    mark = int(input('enter your mark: '))
    ThisPaper = ExaminationPaper(centrenum,candnum)
    if ThisPaper.SetFinalMark(mark) == False:
        print('error mark')
    else:
        ThisPaper.SetGrade(mark,80,70,55)
        print(ThisPaper.GetGrade())
Main()
