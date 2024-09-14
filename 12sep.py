#multiple inheritance :-
# having more than one parent class which have only one child class
# for example we have 2 parent class like area of tringle and area of squre and they both have common child i.e area
# in simple word from 2 base class derived one class
# Hybrid inheritance
# #
class Stud:
    def __init__(self,Name,Rollno):
        self.name=Name
        self.rollno=Rollno

class Marks:
    def __init__(self,Math,Sci,Eng):
        self.math=Math
        self.sci=Sci
        self.eng=Eng

    def TotalMarks(self):
        return self.math+self.sci+self.eng
        

class Result(Stud,Marks):
    def __init__(self, Name, Rollno ,Math,Sci,Eng):
        Stud.__init__(self,Name, Rollno)
        Marks.__init__(self,Math,Sci,Eng)
    def percentage(self):
        res= (self.TotalMarks()/3)
        print(f"Result of Stud {round(res,2)}% ")

    def showRes(self):
        print(f"roll no :{self.rollno}")
        print(f"Student Name :{self.name}")
        print(f"Maths Marks :{self.math}")
        print(f"Science Marks :{self.sci}")
        print(f"English Marks :{self.eng}")
        print(f"Total Marks Obtained{self.TotalMarks()} out of 300")
        self.percentage()


        

Student=Result("Vaishnavi",57,90,95,90)
Student1=Result("Vaishnavi",57,90,95,90)

Student.showRes()
Student1.showRes()





