# Dunder Methods :  x+yi==3+5i

# class Comx:
#     def __init__(self,X,Y):
#         self.x=X
#         self.y=Y

#     def __str__(self) :   # dunder method
#         return f"{self.x} + {self.y}i."
    
#     def __repr__(self):
#         return f"Real part : {self.x} \n Imaginary Part : {self.y}i\n"
        
    
# a=Comx(3,5)     #3+5i
# b=Comx(4,2)
# print(f"Complex number of 3 and 5 is {a} ")
# print(str(a))
# print(repr(a))

# print(f"Complex number of 4 and 2 is {b} ")
# print(str(a))
# print(repr(b))

# output :-
# Complex number of 3 and 5 is 3 + 5i. 
# 3 + 5i.
# Real part : 3 
#  Imaginary Part : 5i

# Complex number of 4 and 2 is 4 + 2i. 
# 3 + 5i.
# Real part : 4 
#  Imaginary Part : 2i
#-------------------------------------------------------------------------------------

#example:2
#Vector :
class Vector:
    def __init__(self,X,Y,Z):
        self.x=X
        self.y=Y
        self.z=Z
    def  __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

vector1=Vector(7,4,3) 
vector2=Vector(3,4,5)
print(str(vector1))
print(str(vector2))

# output :-
# Vector(7i + 4j + 3k)
# Vector(3i + 4j + 5k)
#-------------------------------------------------------------------------
        
