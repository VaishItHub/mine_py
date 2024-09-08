# tuple is declare in "()"
#tuples are not changeable. it is called as immutable data type
'''
myt=(10,20,30,40)
print(type(myt))   '''
'''
mytuple=(10,20,30,"vaishu","danavale")
print("mytuple:",mytuple)
print(mytuple.index("vaishu"))     
print(mytuple.count(10))  '''
# set
# set dose not display doible value
# it is a unorderd collection of unique elements
# it ues "{}"

# myset={ 2,3,4,5,5,4,5,3,6,7,8,9}
# print("set:",myset)
# print(myset)
# myset.add(20)
# print(myset)
# myset.remove(5)
# print(myset)
# myset.discard(20) # it use for if there is no element is not present in set it dose not diaplay the error
# print(myset)
# myset.update({44,45,46,99,90})
# print(myset)


A={12,32,4,5,6,29}
B={1,2,3,7,77,29}
C=A.copy()
A.remove(32)  # using without copy 
# {4, 5, 6, 12, 29}
# {4, 5, 6, 12, 29}
print(A)
print(C)

# output:using copy
# ({4, 5, 6, 12, 29}
# {32, 4, 5, 6, 12, 29})

print("A U B :",A.union(B))
print("A n B :",A.intersection(B))
print("A di B :",A.difference(B))
print("A di B :",B.difference(A))
# output:
# A U B : {1, 2, 3, 4, 5, 6, 7, 12, 77, 29}
# A n B : {29}
# A di B : {12, 4, 5, 6}
# A di B : {1, 2, 3, 7, 77}


