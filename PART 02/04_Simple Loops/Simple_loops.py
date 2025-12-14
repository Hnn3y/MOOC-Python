# Another central technique in programming is repetition, or iteration.
# They are called control structures because essentially they allow you to control which lines of code get executed when.
# While conditional structures allow you to choose between sections of code, iteration structures allow you to repeat sections of code. 
# They are often called loops because they allow the program to "loop back" to some line that was already executed before. 
# The process of executing one repetition of a loop is also referred to as an iteration of the loop.


# --> LOOPS AND HELPER VARIABLES

# The program uses two helper variables. The variable attempts keeps track of how many times the user has typed in a PIN. The variable success is set to either True or False based on whether the user is successful in signing in.

attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    # this is printed if the code was incorrect AND there have been less than three attempts
    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")


# --> Debugging print statements in loops

# --> Concatenating strings with the + operator

