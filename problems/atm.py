class LowBalanceError(Exception):
    pass
class ZeroBalanceError(Exception):
    pass
class NegativeWithdrawalError(Exception):
    pass
class ExceedsDailyLimitError(Exception):
    pass
class InvalidPinError(Exception):
    pass
class WrongPinError(Exception):
    pass
class InvalidPinLenError(Exception):
    pass

try:
    with open("ATM.txt", "w") as file:
        Balance = 150000
        Limit = 75000
        actualpin = 5452
        pin = input("Enter a four-digit pin: ")
        if len(pin) != 4 or not pin.isdigit():
            raise InvalidPinLenError("Invalid Pin length.")
        if int(pin) != actualpin:
            raise WrongPinError("Incorrect PIN entered.")        
        Withdrawal = int(input("Enter the Withdrawal amount: "))
        if Withdrawal < 0:
            raise NegativeWithdrawalError("Withdrawal amount cannot be negative.")
        if Withdrawal > Balance:
            raise LowBalanceError("Insufficient balance for withdrawal.")
        if Withdrawal > Limit:
            raise ExceedsDailyLimitError(f"Withdrawal amount exceeds the daily limit of {Limit}.")
        file.write(f"{Balance}\n{Withdrawal}")

except (InvalidPinLenError, WrongPinError, NegativeWithdrawalError, 
        LowBalanceError, ExceedsDailyLimitError) as e:
    print(f"Error Code: {e}")
    exit()  

except IOError as e:
    print(f"File Operation Error: {e}")
    exit()

try:
    with open("ATM.txt", "r") as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise FileNotFoundError("ATM data file is incomplete.")        
        A = int(lines[0])
        B = int(lines[1])
        amount = A - B
        if amount < 0:
            raise LowBalanceError("Balance is low for withdrawal.")
        elif amount == 0:
            print("Your balance is now zero.")
        else:
            print(f"The withdrawal amount is: {B}")
            print(f"Remaining balance is: {amount}")
            print(f"Available daily limit: {Limit - B}")
            print("Thank you for using XYZ BANK")
except (LowBalanceError) as e:
    print(f"Error Code: {e}")
except ZeroBalanceError as e:
    print(f"Error Code: {e}")
except FileNotFoundError as e:
    print(f"Error Code: {e}") 
except IOError as e:
    print(f"File Operation Error: {e}")