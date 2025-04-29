def keyword(name,address):
    print(f"The name is {name} and address: {address} ")
keyword(name="Navneet",address="Uttarakhand")
keyword(address="Jaipur",name="Karan")
print("\n")

def default(name,work):
    print(f"The name is {name} and work: {work} ")
default("Navneet","Student")
default("Student","Navneet")
default(work = "Doctor",name="Rahul")
print("\n")

def length(names):
    for name in names:
        print(f"My name is : {name}")
A1=["Navneet","Rahul","Kunal"]
A2=["Yashmeet","Ishan"]
length(A1)
length(A2)
