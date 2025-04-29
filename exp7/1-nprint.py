def printf(data, current=1):
    if current > data:  
        return
    print(current)  
    printf(data, current + 1)  

num = int(input("Enter the number: "))
printf(num)