# Conditional statements can also be nested within other Conditional statements. 
# For example, the following program checks whether a number is above zero, and then whether it is Odd or even:

number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")



# With nested Conditional statements it is crucial to get the indentations right. 
# Indentations determine which branches are linked together. 
# For example, an ifbranch and an elsebranch with the same amount of whitespace are determined to be branches of the same Conditional statement.

#The same result can often be achieved using either nested Conditional statements or conditions combined with logical operators. 
# The example below is functionally no different from the example above, in the sense that it will print out the exact same things with the same inputs:

number = int(input("Please type in a number: "))

if number > 0 and number % 2 == 0:
    print("The number is even")
elif number > 0 and number % 2 != 0:
    print("The number is odd")
else:
    print("The number is negative or zero")