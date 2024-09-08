#Ex.1
char=65
for i in range(0,4):
    print(" "*(4-i),end=" ")
    for j in range(0,i+1):
        print((char),end=" ")
        char=char+1
    char=65
    print()   
#      output :
#       65 
#     65 66 
#    65 66 67 
#   65 66 67 68

# Ex.2 
char=1
for i in range(0,4):           
#this for is ues for rows/outer pattern /how many times the print
    print(" "*(4-i),end=" ")
    for j in range(0,i+1):
# this for loop is used to what to print
        print((char),end=" ")
        char=char+1
    char=1
    print()   
#     output :
#      1 
#     1 2 
#    1 2 3 
#   1 2 3 4 

# Ex.3 
alph=65
for i in range(0,4):
    print(" "*(4-i),end=" ")
    for j in range( 0,i+1):
        print(chr(alph),end=" ")
        aplh=alph+1
    alph=65
    print()
#     output :
#      A
#     A A
#    A A A
#   A A A A


char=1
for i in range(0,4):           
#this for is ues for rows/outer pattern /how many times the print
    print((4-i)*" ",end=" ")
    for j in range(0,i+1):
# this for loop is used to what to print
        print((char),end=" ")
        char=char+1
    char=1
    print()   