class Fruit:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Vegetable:
    def __init__(self,name,price):
        self.names=name
        self.prices=price
class Shop(Fruit,Vegetable):
    def __init__(self, fruit_name, fruit_price,veg_name,veg_price):
        Fruit.__init__(self,fruit_name,fruit_price)
        Vegetable.__init__(self,veg_name,veg_price)
    def printf(self,namess):
        self.namess=namess
        print(f"{self.namess} went to shop and got {self.name} for {self.price} and {self.names} for {self.prices} ")
user=Shop("Apple","250","Potato","30")
user.printf("Anurag")
                

        
        