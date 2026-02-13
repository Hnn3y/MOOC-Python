# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately.

num = float(input("Please type in a number: "))

integer = int(num)
decimal = num - integer

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")
