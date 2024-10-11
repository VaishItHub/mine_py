
def additon(a,b):
    try:
        print(a+b)
    except Exception as ec:
        print("only digits are accepted")
#--------------------------------------------------------
def division(a,b):
    try:
        print(a/b)
    except Exception as ec:
        print("only digits are accepted",ec)
#-------------------------------------------------------
def multi(a,b):
    try:
       print(a*b)
        
    except Exception as tp:
        print("invalid input",tp)
