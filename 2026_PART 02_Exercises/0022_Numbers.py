# write a program which asks the user for a number. 
# The program then prints out all integer numbers greater than zero but smaller than the input.

num = int(input("Upper limit: "))
current = 1

while current < num:
    print(current)
    current += 1