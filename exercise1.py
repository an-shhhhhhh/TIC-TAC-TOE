# here's a class defining the attributes of my laptop
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price

l1=Laptop("ASUS","TUF GAMING","60,000")
l2=Laptop("LENOVO","YOGA","90,000")
l3=Laptop("APPLE","MACBOOK","1,20,000")
print(l1.brand_name,l1.model_name,l1.price)
print(l2.brand_name,l2.model_name,l2.price)
print(l3.brand_name,l3.model_name,l3.price)