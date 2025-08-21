# Let's have a look at a program which calculates the sum of three numbers given by the user:

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")

# EXERCISE
data= int(input("How many days? "))
print(f"Seconds in that many days: {data * 24 * 60 * 60}")