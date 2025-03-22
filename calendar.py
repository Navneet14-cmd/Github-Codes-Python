day=int(input("Enter the day: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
if (month%2!=0):
    if (day>0 and day<31):print(f"The next day is {day+1}, month is {month}, year is {year}: ")
    elif (day>=31):  
        day=1 
        month+=1
        if (month<12):print(f"The next day is {day}, month is {month}, year is {year}: ")
        elif (month>=12): 
            month=1
            year+=1
            print(f"The next day is {day}, month is {month}, year is {year}: ")   
        else: print("Invalid input. ")
    else: print("invalid input.")        
elif (month%2==0):
    if (day==29 and month==2):
        day=1
        month+=1
        print(f"The next day is {day}, month is {month},year is {year}")
    elif (day>0 and day<30):print(f"The next day is {day+1}, month is {month}, year is {year}: ")
    elif (day>=30): 
        day=1
        month+=1
        if (month<12):print(f"The next day is {day}, month is {month}, year is {year}: ")
        elif (month>=12): 
            month=1
            year+=1
            print(f"The next day is {day}, month is {month}, year is {year}: ")   
        else: print("Invalid input. ")
    else: print("invalid input.")        