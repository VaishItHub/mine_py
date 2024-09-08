# Formulation :-
#--------------------------------------------------------
#(a+b)^2=a^2+b^2+2ab

# a=(int(input("Enetr value of a:")))
# b=(int(input("Enetr value of b:")))
# ans= (a*a)+(b*b)+(2*a+b)
# print("(a+b)^2 :",ans) 

# output
# Enetr value of a:12
# Enetr value of b:13
# (a+b)^2 : 350
#---------------------------------------------------------------
#Area of circle =(3.14)r*r

# r=int(input("enetr the valu of r"))
# area=(3.14)*(r*r)
# print(f"Area of Circle :{area} sq.cm")

#output
# Area of Circle :9156.24 sq.cm 
#---------------------------------------------------------------
#Volume of Sphere =(4/3)*3.14*r*r*r // (4/3)*3.14*r^3
# from math import *
# r=int(input("enter the value of r"))
# ans= (4/3)*3.14*r*r*r
# print(f" Valume of Sphere :{round(ans,2)} cu.cm")      
#output :
# enter the value of r 4
# Valume of Sphere :267.94666666666666 cu.cm
# when we use   from math import * the ans is :
# enter the value of r 2
# Valume of Sphere :33.49 cu.cm   
#---------------------------------------------------------------
# to find any prime number
# num=int(input("Enetr the number : "))
# flag=1
# for i in range(2,(num//2)+1):
#     if(num%i==0):
#         flag=0
#         print(i)
#         break
# if(flag==1):
#      print(f"{num} is  prime number")
# else:
#     print(f"{num} is not prime number")
# output :- Enetr the number : 19
# 19 is  prime number
#-------------------------------------------------------------
# revers of number
# num=int(input("enetr the number"))
# print(f"num :{num}")       

# temp=str(num)
# print(f"temp :{temp[ :: -1]}")
#output
# enetr the number 9527
# num :9527
# temp :7259
#-----------------------------------------------------------------
# write a progarm to find out enter string is palindrome or not 

num=int(input("Enetr number :"))
temp=num
rev=0
while (num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print ("number is palindrome")
else:
    print ("number is not palindrome")

#output :-
# Enetr string 121
# number is palindrome
# Enetr string 122
# number is not palindrome
#using function
def palindrome(num):
    return str(num)==str(num)[::-1]
number=int(input("enter number"))
if palindrome(number):
    print(f"{number} : is palindrome")
else:
    print(f"{number} : is not palindrome")

#------------------------------------------------------