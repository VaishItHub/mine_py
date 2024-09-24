# 4x²+8x+2
class QuadraticEquation:
    def __init__(self,a,b,c):
        self.A=a
        self.B=b
        self.C=c
    def __str__(self):
        return f"({self.A}x²+{self.B}x+{self.C})"
    def __repr__(self):
        return f"Quar{self.A},{self.B},{self.C}"
    def __add__(self,Q):
        return QuadraticEquation(self.A+Q.A,self.B+Q.B,self.C+Q.C)
    def roots(self):
        if self.A==0:
            print("Root does not exists")
            return[]
        else:
            print("Roots are imaginary")
        delta=((self.B**2)-(4*self.A*self.C))
        print(delta)
        if(delta>=0):
            r1=(-self.B+(delta**0.5))/(2*self.A)
            r2=(-self.B-(delta**0.5))/(2*self.A)
            return[r1,r2]
        else:
            print(-1)
Quadra1=QuadraticEquation(4,8,2)
Quadra2=QuadraticEquation(8,20,6)
print(f"Representation of Quadratic Equation:repr{Quadra1}")
print(f"Addition of Quadratic Equation:{Quadra1+Quadra2}")
print(f"Roots of First Object :{Quadra1.roots()}")
print(f"Roots of Second Object :{Quadra2.roots()}")





    
    

    
    