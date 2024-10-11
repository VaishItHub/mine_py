def double(num):
    return num*2
def squrre(num):
    return num**2
def powerOf(num,power):
    return num**power
def cubeRootOf(num):
    return round(num ** (1./3))
def finfMyAge(BirthYear):
    return 2002-BirthYear
def fact(num):
    if num == 0 or num==1:
        return 1
    else:
        return num *fact(num-1)