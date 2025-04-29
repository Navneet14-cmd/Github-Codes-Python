values=[]
num=0
A0=0
A1=0
A2=0
A3=0
n=int(input("Enter the number of input you want to enter. "))
for i in range (0,n,1):
    num=int(input("Enter your number between 0-3 : "))
    values.append(num)
for i in range (0,n,1):
    if (values[i]==0):
        A0+=1
    elif (values[i]==1):
        A1+=1
    elif (values[i]==2):
        A2+=1
    elif (values[i]==3):
        A3+=1
print("Number of '0' in the list : ",A0)
print("Number of '1' in the list: ",A1)
print("Number of '2' in the list: ",A2)
print("Number of '3' in the list: ",A3)

