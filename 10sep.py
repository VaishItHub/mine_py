# 
# class Emp :
#     def __init__(self,Id,Name,Salary) :
#         self.id=Id
#         self.name=Name
#         self.__sal=Salary

#     def printDetails(self):
#         print(f"Employee Id :{self.id}")
#         print(f"Employee Name :{self.name}")
#         print(f"Employee Salary :{self.__sal}")

#     # for get value
#     @property #getter (we declare function as a property that's why we use @ which we call decorator)
#     def Sal_value(self):
#         return self.__sal
#     #to set value
#     @Sal_value.setter
#     def Sal_value(self,new_value):
#         self.__sal=new_value

    
# emp=Emp(101,'Rajesh',10000)
# #print all the info of emp
# emp.printDetails()

# #print sal before setter
# print(emp.Sal_value)
# #set sal=30000
# emp.Sal_value=30000
# print(emp.Sal_value)


class DigitalWatch :
    def __init__(self,Id,Price,GST=0.28) :
        self.__Id=Id
        self.__Price=Price
        self.__GST=GST


    # def printDetails(self):
    #     print(f"DigiWatch Id :{self.__Id}")
    #     print(f"DigiWatch price :{self.__Price}")
    #     print(f"DigiWatch GST :{self.__GST}")

    @property #getter
    def printbill(self):
        return self.__Price+(self.__Price*self.__GST)
    
    @printbill.setter
    def update_Price(self,New_p):
        self.__Price=New_p
        

    
w1= DigitalWatch (12101,5000)
print(w1.printbill)
w1.update_Price=10000
print(w1.printbill)
        
