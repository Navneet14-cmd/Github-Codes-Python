with open ("file2.txt","w") as file:
    integers=[12,42,155,32,165,98,2424]
    for value in integers:
        file.write(f"{value}\n")
with open ("file2.txt","r") as file:
    values=file.readlines()
    Num=[]
    for value in values:
        number=int(value)
        Num.append(number)
    maxelement=max(Num)
    average=sum(Num)/len(Num)
    count=0
    for value in values:
        if (int(value)>100):
            count+=1
    print("The maximum number is : ",maxelement)
    print("The average is : ",average)
    print("The number of integer >100 are : ",count)