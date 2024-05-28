class SuperMarket:

    def __init__(self,productname,MRP,discountprice):

        self.__productname = productname
        self.__MRP = MRP
        self.__discountprice = discountprice

    def set_productname(self, ProductName):
        self.__productname = ProductName
    
    def set_MRP(self, MRP):
        self.__MRP =MRP

    def set_discountprice(self, discountprice):
        self.__discountprice = discountprice

    def get_productname(self):
        return self.__productname
    
    def get_MRP(self):
        return self.__MRP
    def get_discountprice(self):
        return self.__discountprice
    
    def __str__(self):
        return "Product Name:"+self.__productname+" "+"MRP:"+str(self.__MRP)+" "+"discountprice:"+str(self.__discountprice)

products =[]
n=int(input("no. of items taken"))

for i in range(n):
    productname =input("enter the Product Name:")
    MRP = int(input("enter the maximum price rate:"))
    discountprice = int(input("enter the discounted price:"))
    print()
    Market = SuperMarket(productname,MRP,discountprice)
    products.append(Market) 

print("product detail:\n")

for Market in products :
    print("Product Name:",Market.get_productname())
    print("Maximum Price Rate:",Market.get_MRP())
    print("Dscounted Price:",Market.get_discountprice())
    print()

productname = input("enter the product name\n")

for Market in products:

    
    if Market.get_productname() ==productname:

        print(Market)

        break

else: print("Product Not Found")

productname =input(" \nEnter the productname to remove it")

for Market in products:

    if Market.get_productname() == productname:

        products.remove(Market)
        print("product removed")

        break

else: print("product not found")

productname = input("enter the productname to update the Discountprice")
for Market in products:
    if Market.get_productname()==productname:
        new_price=int(input("enter the new pirce"))
        Market.set_discountprice(new_price)
        print("updated successfully")
        print(new_price)
        break
else:
    print("product not found")

