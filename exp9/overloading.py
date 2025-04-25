class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


P1=Point(15,45)
P2=Point(20,30)
P3=P1+P2

print(P1)  
print(P2)  
print(P3)  