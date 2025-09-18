# The following example checks whether a number given by the user is even or not. 
# Parity can be checked with the modulo operator %, which produces the remainder of an integer division operation. 
# When divided by two, if the remainder is zero, the number is even. 
# Otherwise the number is odd.

number = int(input("Please type in a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
