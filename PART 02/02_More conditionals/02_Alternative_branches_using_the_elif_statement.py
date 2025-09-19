# A conditional statement can be added to with an elif branch. 
# It is short for the words "else if", which means the branch will contain an alternative to the original condition

# Importantly, an elif statement is executed only if none of the preceding branches is executed.
# Let's have a look at a program which determines the winner of a match:

goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")