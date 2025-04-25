students=[]
class student:
    def __init__(self,name,sapid,marks):
        self.name=name
        self.sapid=sapid
        self.marks=marks
        
    def details(self):
        print(f"Name: {self.name} ")
        print(f"SAPID: {self.sapid} ")
        print(f"Marks: Physics: {self.marks['phy']}, Chemistry: {self.marks['chem']}, Maths: {self.marks['maths']} ")
        print("\n")
        
for i in range (1,4,1):
    print(f"Enter the students detail: {i} ")
    name=input("Enter the name for student: ")
    sapid=int(input("Enter the sapid: "))
    marks={
        'phy': int(input("Physics marks are: ")),
        'chem' : int(input("Chemistry marks are: ")),
        'maths' : int(input("Maths marks are: "))           
    }
    students.append(student(name,sapid,marks))
    
print("\nThe details of all the students are : ")
for student in students:
    student.details()