students=[]
average=0
class student:
    def __init__(self,name,sapid,marks):
        self.name=name
        self.sapid=sapid
        self.marks=marks
        
    def display(self):
        print(f"Name: {self.name} ")
        print(f"SAPID: {self.sapid} ")
        print(f"Marks: Physics: {self.marks['phy']}, Chemistry: {self.marks['chem']}, Maths: {self.marks['maths']} ")
    
    def Marks_Percentage(self):
        total=self.marks['phy'] + self.marks['chem'] + self.marks['maths']
        avg=total/300
        percent=avg*100
        print(f"Percentage: {percent}")
    
    def display_result(self):
        if (self.marks['phy']>40 and self.marks['chem']>40 and self.marks['maths']>40 ):
            print("RESULT: Pass \n")
        else:
            print("RESULT: Fail \n")
            
    def average(self,num):
        global average
        total=self.marks['phy'] + self.marks['chem'] + self.marks['maths']
        avg=total/300
        percent=avg*100
        average=average+percent       
        
        
            
n=int(input("Enter the number of students detail you want to enter: "))
for i in range (1,n+1,1):
    print(f"Enter the details of student: {i} ")
    name=input("Enter the name: ")
    sapid=int(input("Enter the sapid: "))
    marks={
        'phy': int(input("Physics marks are: ")),
        'chem': int(input("Chemistry marks are: ")),
        'maths': int(input("Maths marks are : "))        
    }
    students.append(student(name,sapid,marks))
    
print("\nStudent details ") 
for student in students:
    student.display() #display
    student.Marks_Percentage() #percentage
    student.display_result() #pass or fail
    student.average(n)
print("\nClass average: ",average/n)



    
    


