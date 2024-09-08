from array import *
arr =array("i",[12,34,56,67,90])
print(type(arr))
print(arr)
print(arr.typecode)
print(arr.tolist())
# print(arr[0])
# print(arr[1])
print(arr[2])
#print(arr[3])
arr[2]=40
print(arr.tolist())
print(arr.index(40))

value=67
new_v=96
# index=arr.index(34)
# arr[index]=new_v
# print(arr.tolist()) this is the tricky method for replacement
arr[arr.index(67)]=96
print(arr.tolist())
#append :(at the end of arr)
arr.append(100)
print(arr.tolist())
#insert on any index:
arr.insert(0,99)
print(arr.tolist())

print(len(arr))

#list of element : add in array
arr.extend([22,12,30])
arr.extend((22,12,300))
arr.extend({22,12,30})
print(arr.tolist())
# remove any item :
arr.remove(100)
print(arr.tolist())
# remove item using index:
arr.pop()
print(arr.tolist())
arr.pop(2)
print(arr.tolist())
# count:(accurance of item)
print("Occurance (12):",arr.count(12))
#slicing
print("Slicing of array :",arr[0:len(arr):-1])
print("Slicing of array :",arr[len(arr):0:-1])
print("Slicing of array :",arr[::-1])
#reverse:
arr.reverse()
print("rev of array :",arr.tolist())



