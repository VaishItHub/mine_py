#constructor
class Earphones:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color= color
        
        def PrintInvoice(self):
            print("Brand :",self.brand,
          "Price :",self.price,
          "color :",self.color)
        def PairDevice(self,name):
            print("Pairing device...")
            print("ivice Paired successfully with",name)

ap1 = Earphones("BrandName", 50,"Black")
ap1.PrintInvoice()


ap2 = Earphones("Android", 50,"White")
ap2.PrintInvoice()
'''
    def PrintInvoice(self):
        print("Invoice for", self.brand, 
              "earphones. Price:", self.price,
              "earphones. Color:", self.color)

# Create an instance of the Earphones class
ap1 = Earphones("BrandName", 50,"Black")
# Call the PrintInvoice method on the instance
ap1.PrintInvoice()

ap2 = Earphones("Apple", 50,"White")
ap2.PrintInvoice()

# ap1=Earphones("Apple",25000,"White",3)
# print("Company :",ap1.company)
# print("Price :",ap1.price)
# print("Color :",ap1.color)
# print("Battery_Life :",ap1.battery_life)
'''


