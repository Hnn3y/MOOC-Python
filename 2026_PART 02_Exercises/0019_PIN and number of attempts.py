# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321 . 
# The program should then print out the number of times the user tried different codes.

tries = 0
while True:
    pin = input("PIN: ")
    tries += 1

    if pin == "4321":
        if tries == 1:
            print(f"Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {tries} attempts")
        break
    else:
        print(f"Wrong")