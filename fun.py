# input list=[2,4,5,3,9]
# output= nlist=[4,8,10,6,18]
# using for loop
# list=[2,4,5,3,9]
# nlist=[]
# for i in list:
#     nlist.append(i*2)
# print(nlist)

# same program using map function

# mylist=[2,4,5,3,9]
# nlist=list(map(lambda x:x*2,mylist))    # map function performs the coversion of any opersaiom
# print(nlist) 


#ex 2 input=list=[2,4,6,7,3,9,10]
#output= nlist=[2,4,6,10] print even numbers
# list=[2,4,6,7,3,9,10]
# nlist=[]
# for i in list:
#     if i%2==0:
#       print(nlist.append(i))
# print(nlist)

# same program using filter function
# list1=[2,4,5,6,3,9,10]
# nlist=list(filter(lambda x:x%2==0,list1))   filter can cjheck condition and take necedary portion and can neglect the unnecessary portion of the input
# print(nlist)

# ex 3=input=mylist=[2,4,3,7,1]
# output=sum=17
# mylist=[2,4,4,7,1]
# sum=0
# for i in mylist:
#     sum=sum+i
# print(sum)

# same program using reduce function

from functools import reduce
mylist=[2,4,3,7,1]
sum=reduce(lambda a,b:a+b,mylist)   #reduce can combine the whole output into a single output
print(sum)














# # example 2  single inheritance class 
# # class person:
# #     def __init__(self,name,addr) :
# #         self.name=name
# #         self.addr=addr
# # class emp (person):
# #     def __init__(self, name, addr,eid,sal):
# #         super().__init__(name, addr)
# #         self.eid=eid
# #         self.sal=sal
# #     def show(self):
# #         print("name :",self.name)
# #         print("address :",self.addr)
# #         print("edi :",self.eid)
# #         print("salary :",self.sal)

# # e=emp("Vaishnavi","Pune",101,60000)
# # e.show()

# # multilevel 
# class college:
#     def __init__(self,clznm) :
#         self.clznm=clznm

# class hod:
#     def __init__(self,hodnm) :
#         self.hodnm=hodnm 

# class department(college,hod):
#     def __init__(self,dtnm,hodnm,clznm) :
#         hod().__init__(hodnm)
#         college().__init__(clznm)
#         self.dname=dtnm 
#     def show(self):
#         print(self.dname)
#         print(self.hodnm)
#         print(self.clznm)
# d=department("Computer","Mr.roy","RDTC")
# d.show()