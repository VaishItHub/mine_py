from threading import *
# import time
# t1=Thread()
# print(type(t1))

# class mythread(Thread):
#     def __init__(self, id,target):
#         Thread.__init__(self,target=target)
#         self.id=id
#     def printmyid(self):
#         print(f"id : {self.id}")
        
# def hello():
#         print("Hello well-come")
# t1=mythread(target=hello,id=12)
# t1.start()
# t1.join()
# t1.printmyid()

# -----------------------------------------------
# class vaishThread(Thread):
#     def __init__(self,name,t):
#         Thread.__init__(self,target=t)
#         self.name=name
#     def printname(self):
#         print(f"{self.name}")
# def namee():
#     print(" my name is:")
    
# t1=vaishThread(t=namee,name="vaishnavi")
# t1.start()
# t1.join()
# t1.printname()
#--------------------------------------------------------

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
        
#     def addition(self):
#         print(self.num1+self.num2)
        
#     def substraction(self):
#         return(self.num1-self.num2)
    
#     def addAll(self,arr):
#         print(sum(arr))
        
# obj=Calculator(4,5)
# t1=Thread(target=obj.addition)
# t1.start()
# t2=Thread(target=obj.addAll,args=([1,2,3,4,5],))
# t2.start()

class Vaishnavi:
    def __init__(self,fname,mname,lname):
        self.fname=fname
        self.fname=mname
        self.fname=lname
    def display(self):
        print(f"")
        