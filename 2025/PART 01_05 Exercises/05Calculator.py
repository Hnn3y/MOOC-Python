# write a program which asks the user for two numbers and an operation. 
# If the operation is add , multiply or subtract , the program should calculate and print out the result of the operation with the given numbers. 
# If the user types in anything else, the program should print out nothing.

Num1 = int(input("Number 1: "))
Num2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
   result = Num1 + Num2
   print(f"{Num1} + {Num2} = {result}")

elif operation == "multiply":
   result = Num1 * Num2
   print(f"{Num1} * {Num2} = {result}")

elif operation == "subtract":
   result = Num1 - Num2
   print(f"{Num1} - {Num2} = {result}")

else:
   print("Nothing")