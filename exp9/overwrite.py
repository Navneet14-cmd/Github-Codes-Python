class City:
    def __init__(self, name, year):
        self.name=name
        self.year=year

    def printf(self):
        print(f"The name of city in {self.year} is {self.name} ...")
        
class Cityy(City):
    def printf(self):
        print(f"The name of city in {self.year} is {self.name} ...")

class Citz(City):
    def printf(self):
        print(f"The name of city in {self.year} is {self.name} ...")

city1 = City("Jaspur", "2010")
city1.printf()
city2 = Cityy("Ilakh", "2022")
city2.printf()
city3 = Citz("Agra", "2014")
city3.printf()













