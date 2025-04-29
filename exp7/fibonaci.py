def fib(data):
    if (data==1):
        return 0
    elif (data==2):
        return 1
    else: return fib(data-1)+fib(data-2)
num=int(input("Enter the number: "))
for i in range (1,num+1,1):
    print(fib(i))
        