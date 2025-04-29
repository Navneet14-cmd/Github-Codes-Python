balance=150000
dailylimit=75000
class LowBalanceError(Exception): 
    pass
class ZeroBalanceError(Exception):
    pass
class NegativeWithdrawalError(Exception):
    pass
class ExceedsDailyLimitError(Exception):
    pass
class InvalidDetails(Exception):
    pass
class InvalidPinLenError(Exception):
    pass
class atm:
    def __init__(self,name,account,pin):
        self.name=name
        self.account=account
        self.pin=pin
    def check(self,name,account,pin):
        if (self.name=="Navneet") and (self.account==5085) and (self.pin==5354):
            pass
        else:
            raise InvalidDetails("Enter valid Details. ")
    def amount(self, amount):
        global balance
        if (amount > dailylimit):
            raise ExceedsDailyLimitError(f"Withdrawal amount exceeds the daily limit of {dailylimit}.")
        elif (amount > balance):
            raise LowBalanceError("Insufficient balance for withdrawal.")
        elif (amount > 0):         
            balance=balance-amount
            if balance==0:
                raise ZeroBalanceError("Your balance is zero now.")
            return balance
        else:
            raise NegativeWithdrawalError("Withdrawal amount must be positive.")
    def printresult(self, withdrawal):
        print("Thank you for Using XYZ Bank:")
        print("Current Balance:", withdrawal)
try:
    print("Welcome to XYZ Bank, Kindly Enter Your Details\n")
    name=input("Enter Your User Name: \n")
    account=int(input("Enter Your Account Number: \n"))
    pin=int(input("Enter Your 4-digit Pin:\n"))    
    if len(str(pin))!=4:
        raise InvalidPinLenError("Invalid PIN length.")    
    user=atm(name,account,pin)
    user.check(name,account,pin)
    wish=int(input("Enter the amount you want to withdraw: "))
    withdrawal=user.amount(wish)
    user.printresult(withdrawal)
except (LowBalanceError, ZeroBalanceError, NegativeWithdrawalError,ExceedsDailyLimitError, InvalidPinLenError, InvalidDetails) as e:
    print(f"Error Code: {e}")
