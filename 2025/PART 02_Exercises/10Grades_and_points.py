# write a program which asks for the amount of points received and then prints out the grade achieved according to the table.

points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
   print(f"Grade: impossible!")
elif points <= 49 :
   print(f"Grade: fail")
elif points <= 59 :
   print(f"Grade: 1")
elif points <= 69 :
   print(f"Grade: 2")
elif points <= 79 :
   print(f"Grade: 3")
elif points <= 89 :
   print(f"Grade: 4")
elif points <= 100 :
   print(f"Grade: 5")
