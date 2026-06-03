# Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

L1 = input("1st letter: ")
L2 = input("2nd letter: ")
L3 = input("3rd letter: ")

if L1 > L2:
    if L1 > L3:

        if L2 > L3:
            print(f"The letter in the middle is {L2}")
        else:
            print(f"The letter in the middle is {L3}")
    else:
        print(f"The letter in the middle is {L1}")
else:
    if L2 > L3:
        if L1 > L3:
            print(f"The letter in the middle is {L1}")
        else:
            print(f"The letter in the middle is {L3}")
    else:
        print(f"The letter in the middle is {L2}")