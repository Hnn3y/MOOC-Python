# Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points = int(input("How many points [0-100]: "))
if points < 0 or points > 100:
    print(f"Grade: impossible!")
elif points < 50:
    print(f"Grade: fail")
elif points < 60:
    print(f"Grade: 1")
elif points < 70:
    print(f"Grade: 2")
elif points < 80:
    print(f"Grade: 3")
elif points < 90:
    print(f"Grade: 4")
else:
    print(f"Grade: 5")