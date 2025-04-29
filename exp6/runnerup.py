n=int(input("Enter the number of student's data you want to enter: "))
data=[]
greatest=0
runner=0
for i in range (1,n+1,1):
    num=int(input(f"Enter the score of student no. {i} : "))
    data.append(num)
greatest=data[0]
for i in range (0,n,1):
    if (greatest>data[i]):
        if (data[i]>runner):
            runner=data[i]
    elif (greatest<data[i]):
        runner=greatest
        greatest=data[i]
print("The runner up  is : ",runner)