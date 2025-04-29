n1=int(input("Enter the number of fruits you want to add in set1: "))
n2=int(input("Enter the number of fruits you want to add in set2: "))
s1=set()
s2=set()
s3=""
s4=""
for i in range (0,n1,1):
    s3=(input("Enter the fruit name in s1: "))
    s1.add(s3)    
for j in range (0,n2,1):
    s4=(input("Enter the fruit name in s2: "))
    s2.add(s4)
print("Fruits which are in both set: ",s1.intersection(s2))
print("Fruits only in S1 but not in s2: ",s1.difference(s2))
print(len(s1.union(s2)))
