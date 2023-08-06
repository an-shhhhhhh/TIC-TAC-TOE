class Laptop:
    def __init__(self,brand,model,price):
        # instance variables
        self.brand=brand
        self.model=model
        self.price=price
        self.laptop_name=brand+" "+model

    def discount(self,price,percent):
        return print(price-percent*price/100)


lapi1=Laptop("ASUS","TUF GAMING","60,000")
print(lapi1.brand,lapi1.model,lapi1.price)
print(lapi1.discount(60000,10))