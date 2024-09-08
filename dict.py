
# dict is ues "{key:value}" ker value pair
# we can not use dublicate key but we can assing similar value 
First={
    "Name":"Vaishnavi",
    "Mark":8.88,
    "Addr":"Bare",
    "Pin-Code":412206,
}
print(type(First))
#<class 'dict'>
print(First)
#{'Name': 'Vaishnavi', 'Mark': 8.88, 'Addr': 'Bare', 'Pin-Code': 412206}
print(First["Name"])
print(First["Mark"])
print(First["Addr"])
# Vaishnavi
# 8.88
# Bare

# value print by key using for loop
for key in First:
    print(First[key])
# Vaishnavi
# 8.88
# Bare
# 412206



mydict={
    "Name":"Vaishnavi",
    "Age":22, 
    "City":"Pune"
}
#update or add new data in dictionary
mydict.update({"country":"India","Mob.No":1234567890})
print(mydict)
#print only keys
print(mydict.keys())
#print only values
print(mydict.values())
#print only itens
print(mydict.items())
# for change the values
mydict["Name"]="Radh"
print(mydict["Name"])
mydict["Age"]=30
print(mydict["Age"])
print(mydict)
# use for loop to print at a time
for key in mydict:
    print(key,":",mydict[key])
# using del(delete) we can del the existing data    
del mydict["Age"]
print(mydict)
# for print length
print("Length:",len(mydict))
# output :Length: 4