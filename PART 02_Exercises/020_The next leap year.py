# write a program which asks the user for a year, and prints out the next leap year.

while True: 
  year = int(input("Year: "))

  if year // 4:
   print(f"The next leap year after {year} is ")