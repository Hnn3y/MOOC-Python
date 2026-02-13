# input() always gives you a string, even if the user types a number.

# You can’t do math with strings directly.

# To do calculations, you must cast (convert) the string into a number.


input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2021: {2025 - year}" )

# Ask for year of birth
input_str = input("What is your year of birth? ")

# Convert the string into an integer
year = int(input_str)

# Do calculation (age in 2021)
age = 2021 - year

# Print result
print("You were", age, "years old in 2021")


# Reading the input with the input function and converting it with the int function can be achieved in one go:
year = int(input("Which year were you born? "))
print(f"Your age at the end of the year 2021: {2021 - year}" )

name = input("What is your name? ")
input_str = input("Which year were you born? ")
print(f"Hi {name}, you will be {2021 - int(input_str)} years old at the end of the year 2021" )