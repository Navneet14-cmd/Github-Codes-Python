class Principal:
    def __init__(self,name,school):
        self.name=name
        self.school=school
class Teacher(Principal):
    def printf(self, teacher):
        self.teacher = teacher
        print(f"{self.teacher}'s Principal name is: {self.name} and works on {self.school} school")

user=Teacher("Rahul","St Joseph")
user.printf("Anurag") 