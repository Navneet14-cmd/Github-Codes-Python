try:
    N=int(input("Enter the number: "))
except:
    ValueError
    print("Error Code: Invalid Input of N ")
    N=0
for i in range (N):
    try:
        a,b=input().split()
        a=int(a)
        b=int(b)
        print(a//b)
    except ZeroDivisionError as e:
        print(f"Error Code: {e} ")
    except ValueError as e:
        print(f"Error Code is : {e} ")
    finally:
        print("The code is executed ")