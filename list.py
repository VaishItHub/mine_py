
# ;ist are immutable data type use symbol "[]"
#  Ex .1
# l1=[10,20,30,40,50]
# print(l1)
# print(type(l1))

# # Ex .2
# mylst=[23,22.5,"Vaishnavi","Danavale"]
# print(mylst)

# #[10, 20, 30, 40, 50]
# #<class 'list'>

# #[23, 22.5, 'Vaishnavi', 'Danavale']

# #Ex .3
# l1=[33,24,35,66,99]
# print("list :",l1)
# print(l1[2])
# print(l1[-4])

# # list : [33, 24, 35, 66, 99]
# # 35
# # 24

# #Ex .4 Print second last num
# l2=[10,2,3,30,445,3,55]
# print(l2.sort())
# print("Second large number is :",l2[-2])

# # None
# # Second large number is : 55

# #Ex .5 revers num
# print("reversed list:",l2.sort(reverse=True))
# print("list:",l2)

# #list: [445, 55, 30, 10, 3, 3, 2]

# #Ex .6 replace list element
# print("Origrnal list:",l2)
# l2[2]=5
# print("list after replacing:",l2)

# # Origrnal list: [445, 55, 30, 10, 3, 3, 2]
# # list after modify: [445, 55, 5, 10, 3, 3, 2]

# # Ex .7 remove
# print("list:",l2)
# l2.remove(5)
# print("list after removing element :",l2)

# # list: [445, 55, 5, 10, 3, 3, 2]
# # list after removing element : [445, 55, 10, 3, 3, 2]

# #Ex .8 insrt/add data in list(appent)
# print("Origrnal list:",l2)
# l2.append(90)
# print("list :",l2)
# # append add element at end
# #Origrnal list: [445, 55, 10, 3, 3, 2]
# #list : [445, 55, 10, 3, 3, 2, 90]
# l2.insert(0,400)
# print("List using inser:",l2)
# # add element at any Index num
# # list : [445, 55, 10, 3, 3, 2, 90]
# # List using inser: [400, 445, 55, 10, 3, 3, 2, 90]

# # ex.9 to find index of element in list
# lst=[12,3,12,30,40,40,50,60,5,1,3,4,10]
# print("index of 5:",lst.index(5))

# #ex .10 count number of numbers
# print("count of 40:",lst.count(40))

# #count of 40: 2

# #min/max/sum/revers element
# print("min element:",min(lst))
# print("max element:",max(lst))
# print("sum element:",sum(lst))
# lst.sort()
# print("list after sorting:",lst)
# lst.reverse()
# print("list after reversing:",lst)

# # min element: 1
# # max element: 60
# # sum element: 270
# # list after sorting: [1, 3, 3, 4, 5, 10, 12, 12, 30, 40, 40, 50, 60]
# # list after reversing: [60, 50, 40, 40, 30, 12, 12, 10, 5, 4, 3, 3, 1]


#check the  list element if the character is vowel or not then append it into the another list
# vo=[]
# co=[]
# lst=int(input("enter no of elemet"))
# for i in range(0,lst):
#     ch=input("enter the character")
#     if ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" or ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#         vo.append(ch)
#     else:
#         co.append(ch)

# print("this character are vowel",vo)            
# print("constant character",co)            

#output  
# enter no of elemet5
# enter the characterA
# enter the characterI
# enter the characterO
# enter the characterv
# enter the characterU
# this character are vowel ['A', 'I', 'O', 'U']
# constant character ['v']

# year is leap year or not
# y=int(input("enter the year"))
# if y%4==0:
#     print(" This is Leap Year!")
# else:
#     print(" This is not Leap Year !")


# output :
# enter the year 2024
#  This is Leap Year !
# enter the year 2013
#  This is not Leap Year !
