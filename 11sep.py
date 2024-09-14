# multi-level inheritence:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def personDetails(self):
        print(f"{self.name} is {self.age} years old.")


        
class Employee(Person):
    def __init__(self,name,age,Id,Salary):
        super().__init__(name,age)
        self.id=Id
        self.salary=Salary
    def Empdetails(self):
        print(f"Emp Id {self.id} has {self.salary} salary per month.")


class Devop(Employee):
    def __init__(self,name,age,Id,Salary,Dept,Project) :
        super().__init__(name,age,Id,Salary)
        self.dept=Dept
        self.project=Project

    def Devopdetails(self):
        print(f"Developer is working in {self.dept} Department he work on project(self.project)")

    def RecortDevop(self):
        print(f"Emp id of Developer :{self.id}")
        print(f"Name of Developer :{self.name}")
        print(f"Department of Developer :{self.dept}")
        print(f"Developer work on :{self.project}")
        print(f"Developer has {self.salary} salary")
d1= Devop ('Vighanesh',25,21,50000,'AI','GPT-5')
d1.RecortDevop()