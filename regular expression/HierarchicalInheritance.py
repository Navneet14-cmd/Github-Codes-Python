class A:
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