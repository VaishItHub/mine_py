# public 
# private
# protected
# #
# class MainDemo:
#     def __init__(self) :
#         self.a=10
#         self._b=20
#         self.__c=30

# a=MainDemo()
# print(a.a)
# print(a._b)
# print(a._MainDemo__c)
        
# overriding 
# #
# print(" Example of Overring Polymorphism :")
# class Parent:
#     def given(self) :
#         print("Hello,I am Parent Class.")

#     def add(self,a,b):
#         print("Addition of a and b :",a+b)
            

# class Child(Parent):
#     def given(self):
#         print("Hello,I am Child class.")

#     def add(self,nums):
#         sum=0
#         for n in nums:
#             sum +=n
#         print(f"Addition is : {sum}")
        
# ram=Parent()
# raju=Child()

# ram.given()
# ram.add(2,3)
# raju.given()  
      

# Ex=2
class Shape():
    def __init__(self,Name):
        self.name=Name
        
    def Area(self):
        pass


class Square(Shape):
    def __init__(self, Side):
        self.side=Side  

    def Area(self):
        print(self.side ** 2)

sqr=Square('Cirle',10)
sqr.Area()

Ex =3


