# write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. 
# If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for Converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

temp = float(input("Please type in a temperature (F): "))

conversion = (temp - 32) * 5/9

print(f"{temp} degrees Fahrenheit equals {conversion} degrees Celsius")

if conversion < 0:
   print(f"Brr! It's cold in here!")