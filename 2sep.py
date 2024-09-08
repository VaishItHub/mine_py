# Function we use def keyword for declare the function in python
# def add():
#     a=int(input("enter the value of a"))
#     b=int(input("enter the value of b"))
#     print(f"Addition of {a} and {b} is :",a+b)
# add()
# output :-
# enter the value of a 12
# enter the value of b 12
# Addition of 12 and 12 is : 24
#-----------------------------------------------------------

def gread():
    mark=[]
    lst=int(input("enter no of subject"))
    for i in range(0,lst):
        num=input("enter the marks")
        mark.append(num)
    print(f"gread : {round(sum(mark)/len(mark),2)}")
print()
gread()


    