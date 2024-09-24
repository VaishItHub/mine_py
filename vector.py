# # 2x²+4x+2
# class QuaradaticEquation:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c

#     def __str__(self):
#         return f"{self.a}x²+{self.b}x+{self.c}"
    
#     def __repr__(self) -> str:
#         return f"Quar {self.a},{self.b},{self.c}"
    
#     def __add__(self,e):
#         return QuaradaticEquation(self.a+e.a,self.b+e.b,self.c+e.c)
#     def roots(self):
#         if self.a==0:
#             print("Roots doesn't exits!")
#             return []
#         # else:
#         #     print("root are imagenary")
#         delta= ((self.b**2)-(4*self.a*self.c))
#         print(delta)

#         if (delta>=0):
#             r1=(-self.b+(delta**0.5))/(2*self.a) 
#             r2=(-self.b-(delta**0.5))/(2*self.a) 
            
#             return [r1,r2]
#         else:
#             print("root are imagenary")
#             return-1
# e1= QuaradaticEquation(2,4,2)
# e2=QuaradaticEquation(3,10,7)
# e3=QuaradaticEquation(8,20,6)
# e4=QuaradaticEquation(0,2,6)
# print(e1+e2+e3)
# print(e1.roots())
# print(e2.roots())
# print(e3.roots())
# print(e4.roots())

class Vector:
    def __init__(self,a,b,c):
        self.A=a
        self.B=b
        self.C=c
    def __str__(self) :
        return f"({self.A}i+{self.B}j+{self.C}k)"
    def __repr__(self):
        return f" vector:{self.A}i+{self.B}j+{self.C}k"
    def __len__(self):
        return int((self.A**2+self.B**2+self.C**2)**(0.5))
    def __add__(self,v):
        return Vector(self.A+v.A,self.B+v.B,self.C+v.C)
v=Vector(2,3,4)
v2=Vector(4,6,4)
print(f"Vector of v :{v}")
print(f"Vector of v2 :{v2}")
print(f"Representation of Vector is : {repr(v)}")
print(f"Length of Vector v is : {len(v)}")
print(f"Length of Vector v2 is : {len(v2)}")
print(f"addition of two vectors are : {v+v2}")
    


