# write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of Portions and prints out the total cost. The price of a single portion is 5.90.

# Two examples of the program's execution:

# Sample output
# Please tell me your name: Kramer 
# How many portions of soup? 2 
# The total cost is 11.8 Next please!

name =input("Please tell me your name: ")

if name == "Jerry":
   print(f"Next please!")
else:
   portions = int(input("How many portions of soup? "))
   price = 5.90
   cost= portions * price

   print(f"The total cost is {cost} Next please!")