# write a program which asks for the Hourly wage, hours worked, and the day of the week. 
# The program should then print out the daily wages, which equal the Hourly wage multiplied by hours worked, except on Sundays when the Hourly wage is doubled.

hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day = input("Day of the week: ")


if day == "Sunday":
   daily_wage = (hourly_wage * 2) * hours_worked
else:
   daily_wage = hourly_wage * hours_worked

print(f"Daily wages: {daily_wage} euros")
