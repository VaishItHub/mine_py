# myli=[2 ,3,4,5,6,7]
# print (f" mylist is : {myli}")
# newli=[]
# for i in myli:
#     newli.append(i*2)
# print (f" newlist is : {newli}")


# using map function
# myli=[2 ,3,4,5,6,7]
# print (f" mylist is : {myli}")
# newli=list(map(lambda x:x*2,myli))
# print (f" newlist is : {newli}")
#-------------------------------------


# Ex 2
# myli=[2 ,3,4,5,6,7,8,10]
# newli=[]
# print (f" mylist is : {myli}")
# for i in myli:
#     if i %2==0:
#         newli.append(i)
# print (f" newlist is : {newli}")

# # using filter function for even num only
# myli=[2 ,3,4,5,6,7,8,10]
# newli=[]
# print (f" mylist is : {myli}")
# newli=list(filter(lambda a:a%2==0,myli))
# print (f" newlist is : {newli}")


# using filter function for odd num only
# myli=[2 ,3,4,5,6,7,8,10]
# newli=[]
# print (f" mylist is : {myli}")
# newli=list(filter(lambda a:a%2!=0,myli))
# print (f" newlist is : {newli}")
#------------------------------------------

# myli=[2 ,3,4,5,6,7,8,10]
# sum=0
# for i in myli:
#     sum+=1
# print(sum)

#reduce function 

# from functools import reduce
# mylist=[2,3,45,6,7]
# sum=reduce(lambda a,b:a+b,mylist)
# print(f"addition of the list element : {sum}")

#---------------------------------------------
