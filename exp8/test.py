class LowBalanceError(Exception):
    pass
class ZeroBalanceError(Exception):
    pass

with open ("Bankstatement.txt","w") as file:
    try:
        Balance=int(input("Enter the Balance : "))
        Withdrawal=int(input("Enter the Withdrawal amount: "))
        file.write (f"{Balance}\n{Withdrawal}")
    except ValueError:
        print("Enter a valid Numeric Value. ")
        exit()
try:
    with open ("Bankstatement.txt","r") as file:
        lines=file.readlines()
        A=int(lines[0])
        B=int(lines[1])
        amount=A-B
        
        if (amount<0):
            raise LowBalanceError("Balance is low for Withdrawal. ")
        elif (amount==0):
            raise ZeroBalanceError("Your Balance is Zero Now. ")
        print(f"The withdrawal amount is: {B}\nRemaining balance is: {amount}")
        
except FileNotFoundError as e:
    print(f"Error Code : {e}")
except LowBalanceError as e:
    print(f"Error Code : {e}")
except ZeroBalanceError as e:
    print(f"Error Code: {e}")
except ValueError as e:
    print(f"Error Code: {e} ")
        
        
            
            
    
        