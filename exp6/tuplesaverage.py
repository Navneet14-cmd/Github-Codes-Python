values = ()
avg=0
num=int(input("How many values would you like to add to the tuple? "))
for i in range(num):
    value = int(input("Enter a value: "))
    values = values + (value,) 
    avg=avg+values[i]   
print("The average is : ",avg/num)

