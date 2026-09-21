# Design a simple Banking System in Python using Custom Exception Handling.
# Requirements:
# If withdrawal amount is greater than balance, raise a custom exception → InsufficientBalanceError.
# If withdrawal amount is negative, raise a custom exception → InvalidAmountError.
# If withdrawal amount is zero, raise a custom exception → ZeroAmountError.
# If withdrawal is valid, update the balance and display the remaining balance.

Amount = 5000
withdrawal = int(input("Enter the withdrawl amount "))

class InsufficientBalanceError(Exception):
    pass   

# if withdrawal Amount is negative 
class InvalidAmountError(Exception):  
    pass

# If withdrawal amount is zero, raise a custom exception → ZeroAmountError.
class ZeroAmountError(Exception):
    pass

# If withdrawal is valid, update the balance and display the remaining balance.
class RemainingBalance(Exception):     
    pass

try:
    if withdrawal > Amount:
        raise InsufficientBalanceError(
         "you have not amount more then withdrawl Amount....."
        )
    elif withdrawal < 0:
        raise InvalidAmountError(
            "you are not withdraw because withdrawl Amount is negative "
        )
    elif withdrawal == 0:
        raise ZeroAmountError(
            "withdrawl Amount is Zero your current balance are the same "
        )
    else:
        print(f"your withdraw the Amount are successful -> {withdrawal}")
    # jab koye test case na chalega to last wala custom exception chalega 
    raise RemainingBalance(f"your current Available Balance {Amount - withdrawal}")
    print("withdrawl are successful")
except InsufficientBalanceError as e:
    print(f"Bank Provide the msg : {e}")
except InvalidAmountError as error:
    print(f"Bank Provide the msg : {error}")  
except ZeroAmountError as e:
    print(f"Bank Provide the msg : {e}")  
except RemainingBalance as e:
    print(f"Bank Provide msg : {e}")
