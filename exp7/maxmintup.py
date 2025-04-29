tupley=lambda temp: ((max(temp),min(temp)))
List=[]
num=int(input("Enter the number of element you want to add: "))
for i in range (1,num+1,1):
    n=int(input("Enter the number: "))
    List.append(n)
print(tupley(List))