class Fruit: #Multiple Inheritance
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
user=Shop("Apple","250","Potato","30\n")
user.printf("Anurag")


class A: #Hierarchical Inheritance
    def func(self):
        return "My name is: "
class B(A):
    def funcs(self):
        return (A.func(self))+"Rahul"
class C(A):
    def funcse(self):
        return (A.func(self))+"Anurag"
user1=B()
user2=C()
print(user1.funcs())
print(user2.funcse())


class A: #Multilevel Inheritance
    def __init__(self,name,id):
        self.name=name
        self.id=id
class B(A):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.names=self.name+"Singh"
        self.ids=self.id+"000"
class C(B):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.namess=self.names+"*"
        self.idss=self.ids+"1"
        print(f"Name = {self.namess} and ID = {self.idss} ")
user=C("Navneet","592")


class Principal: #Single Inheritance
    def __init__(self,name,school):
        self.name=name
        self.school=school
class Teacher(Principal):
    def printf(self, teacher):
        self.teacher = teacher
        print(f"{self.teacher}'s Principal name is: {self.name} and works on {self.school} school")

user=Teacher("Rahul","St Joseph")
user.printf("Anurag") 


