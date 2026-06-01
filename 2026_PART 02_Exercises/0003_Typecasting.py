# When programming in Python, we often need to change the data type of a value. 
# For example, a floating point number can be converted into an integer with the function int:

# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately.

number = float(input("Please type in a number: "))

int_num = int(number)
float_num = number - int_num

print(f"Integer part: {int_num}")
print(f"Decimal part: {float_num}")