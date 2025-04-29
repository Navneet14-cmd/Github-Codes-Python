import math
def cube(data):
    sum=0
    for i in range (1,data,1):
        sum=sum+math.pow(i,3)
    return sum
num=int(input("Enter the number: "))
print((cube(num)))

    