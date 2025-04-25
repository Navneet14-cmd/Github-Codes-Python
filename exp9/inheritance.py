class Fruit:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Vegetable:
    def __init__(self,names,prices):
        self.names=names
        self.prices=prices
class Shop:
    def __init__(self,fruit_name,fruit_price,veg_name,veg_price):
        Fruit.__init__(self,fruit_name,fruit_price)
        Vegetable.__init__(self,veg_name,veg_price)
    def printf(self,namey):
        self.namey=namey
        print(f"{self.namey} went to shop and bought {self.name} for {self.price} ")