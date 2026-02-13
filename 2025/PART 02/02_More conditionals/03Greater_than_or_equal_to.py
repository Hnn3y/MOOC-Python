# write a program which asks for two integer numbers. 
# The program should then print out whichever is greater. 
# If the numbers are equal, the program should print a different message.


# Some examples of expected behaviour:
#Please type in the first number: 5
#Please type in another number: 3
#The greater number was: 5

first_num = int(input("#Please type in the first number: "))
second_num = int(input("#Please type in another number: "))

if first_num > second_num:
   print(f"The greater number was: {first_num}")
elif second_num > first_num:
   print(f"The greater number was: {second_num}")
else:
   print(f"The numbers are equal!")