# write a program which asks for the names and ages of two persons. 
# The program should then print out the name of the elder.

# Some examples of expected behaviour:
#Person 1:
#Name: Alan
#Age: 26
#Person 2:
#Name: Ada
#Age: 27
#The elder is Ada

print(f"Person 1:")
first_name = input("Name: ")
first_age = int(input("Age: "))

print(f"Person 2:")
second_name = input("Name: ")
second_age = int(input("Age: "))

if first_age > second_age:
   print(f"The elder is {first_name}")
elif second_age > first_age:
   print(f"The elder is {second_name}")
else:
   print(f"{first_name} and {second_name} are the same age")