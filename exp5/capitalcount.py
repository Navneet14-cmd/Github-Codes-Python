n=(input("Enter the string: "))
a=len(n)
c=[]
count=0
for i in range(0,a,1):
    c.append(n[i]) # c=c+n[i]
    if (64<(ord(c[i]))<91):
        count+=1
print(count)