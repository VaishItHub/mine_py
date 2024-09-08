# inheritance
# A class can inherit properties and methods from another class.
# defination:-
#         1) The ability of object of one class to acquire the properties 
#           of object of another class is known as "Inheritence".
#         2)A class derived from another class is known as Inheritance.
#         3)a class can inherites properties and its method from aonther class (parent/child)relationship.
#syntax:-
#        class p_class(object):def __init__(self):
# super:-
#       we use the super kryword to get access of parent class inheritance
#formal parameters :-
#         they work as a local variable and there scope  is only for current scope(block scope)
# actual parameter:
#        this parameter are push during the function
#class Att:-
#      they are variabls which defines the members of bojects(properties)
#instance attribute :-
#        they are the actual records which stores data for there curspoding object
# notes:-class attributes don't need to allocate the memory on the other hand when we create object (instantiat obj) allocates memory
# default parameter= they are functions argument which has default value.
#self keyword= referance of current object.
#" " .join :- this is uesed for covert into string

class Computer :
    def __init__(self,ip,pro,op,price,os):
        self.input_device =ip
        self.processor =pro
        self.output_device =op
        self.price=price
        self.operating_system=os

    def display_details(self):

        #" & " .join :- this is uesed for covert into string
        print("input Device Connected :"," & ".join(self.input_device))
        print("input processor Connected :",self.processor)
        print("op:"," & " .join(self.output_device))
        print("price :",self.price)
        print("Operating_system of Device :",self.operating_system)

# comp= Computer(["keyboard","mouse"],"CPU-Intel",["Monitor","Speaker"],5000,"Window")
# comp.display_details()

# comp1= Computer(["keyboard","mouse"],"CPU-Intel-i9",["Monitor","Speaker"],50000,"Window")
# comp1.display_details()

class Mobile(Computer):
    def __init__(self, ip, pro, op, price, os,ch_type,mgpx,network="No"):
        super().__init__(ip, pro, op, price, os)
        self.charging_type=ch_type
        self.camera_pixel=mgpx
        self.network=network

    def show_details(self):
        self.display_details()
        print("camera details :",self.camera_pixel)
        print("mob price :",self.price)
        print("network of mobile :", self.network,"\n")

        

m1=Mobile(["v_keyboard","touch-pad"],"Sanpdragon-680",["display","speaker"],35000,"Android-14","C type",64,"Yes")
m1.show_details()

m2=Mobile(["v_keyboard","touch-pad"],"Sanpdragon-680",["display","speaker"],40000,"Android-14","C type",64,)
m2.show_details()
