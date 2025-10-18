# write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

Letter1 = input("1st letter: ")
Letter2 = input("2nd letter: ")
Letter3 = input("3rd letter: ")

if Letter1 > Letter2 and Letter1 < Letter3:
    # Letter1 is between Letter2 and Letter3
    middle = Letter1
elif Letter1 < Letter2 and Letter1 > Letter3:
    # Letter1 is between Letter3 and Letter2
    middle = Letter1
elif Letter2 > Letter1 and Letter2 < Letter3:
    # Letter2 is between Letter1 and Letter3
    middle = Letter2
elif Letter2 < Letter1 and Letter2 > Letter3:
    # Letter2 is between Letter3 and Letter1
    middle = Letter2
else:
    # Letter3 must be in the middle
    middle = Letter3

print(f"The letter in the middle is {middle}")