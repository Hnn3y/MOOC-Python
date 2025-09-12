# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately.

num = float(input("Please type in a number: "))

print(f"Integer part: {int(num)}")
print(f"Decimal part: {num:.2f}")
