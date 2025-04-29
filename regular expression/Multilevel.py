class A:
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


