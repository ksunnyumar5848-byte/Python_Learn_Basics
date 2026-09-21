

# Write a Python program to take user input and convert it into integer. Handle ValueError if input is invalid.


"""
try:
    number=int(input("Enter your name "))
    print(f"ager convert huwa to try block excute huga {number}")
except ValueError as error:
    print("string are not convert into integer") 
    print(f"mere ko ye  error provide kar raha hai {error}")


# Write a program to divide two numbers. Handle ZeroDivisionError if denominator is zero.

try:
    divident=1000
    divisor=0
    result=divident/divisor
    print(f"ager mere ko error na de {result}")
except ZeroDivisionError as error:
    print(f"zero are not divisble by any number and error--->{error}")




# Write a program to access an element from a list. Handle IndexError if index is out of range.


# Write a program to open a file. Handle FileNotFoundError if file does not exist.


try:
    with open("myfile.txt","w") as file:
        file.write("hi i am new file \n")
        file.write("hi i am the seconds line ")
except FileNotFoundError:
    print(" mere ko file nahi mila ")        



# Write a program to access a dictionary key. Handle KeyError if key is missing.

try:
    info={
        "name":"Rohit kumar ",
        "age":20,
        "data":"Mydata "
    }

    print(info)
    print(info["name"])
    print(info["location"])
    print(f"if have no any error is then my list data is \n {info}")  
except KeyError as err:
    print(f"try block are not will be works because \n---->:{err}  provide ")   

    
# Write a program to convert a string into integer. Handle exception if conversion fails.
try:
    string=int(input("Enter the string "))

    print(f" conversion are the successful !..->{string}")
except ValueError as e:
    print(f"this conversion are wrong way ....! {e}")    

# Write a program to take two numbers from user and print their sum. Handle exception if input is invalid.
try:
    num1=input("Enter the number ")
    num2=int(input("Enter the seconds number "))
    sum=num1+num2
    print(f"the sum of two number is {sum}")
except ValueError as e:
    print(f"input are invalid {e}")
except TypeError as err:
    print(f"wrong way input form the user {err}")  

       
# Write a program that always prints "Program Finished" in the finally block.
try:
   teacher=input("hello sir what`s  your name bro")
   print(f"oo.. sunny  my  name is :{teacher}") 
except TypeError:
   print("if error exitx then not work try block ")  
finally:
   print("oh.. sunny are are you lat program finished ")    


   

# Write a program to modify a tuple. Handle exception if modification is not allowed.
try:
    Employee=("sunny " ,20, "age","hazaribag ")

    print(Employee[0])
    Employee[0]="puja"
    print(Employee)
except TypeError as error:
    print("modifaction are not allow afer creating the tuples ")    
finally: 
    print("dont, waries bro  plese cheack the your code  way are the error ")    
""" 







