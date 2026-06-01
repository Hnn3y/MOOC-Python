# Please write a program which asks for two integer numbers.
# The program should then print out whichever is greater.
# If the numbers are equal, the program should print a different message.

int_1 = int(input("Please type in the first number: "))
int_2 = int(input("Please type in another number: "))

if int_1 > int_2:
    print(f"The greater number was: {int_1}")
elif int_2 > int_1 :
    print(f"The greater number was: {int_2}")
else:
    print(f"The numbers are equal!")