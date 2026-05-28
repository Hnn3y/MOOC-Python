# Please write a program which asks for the names and ages of two persons. 
# The program should then print out the name of the elder.

print(f"Person 1:")
name_1 = input("Name: ")
age_1 = int(input("Age: "))

print(f"Person 2: ")
name_2 = input("Name: ")
age_2 = int(input("Age: "))

if age_1 > age_2:
    print(f"The elder is {name_1}")
elif age_2 > age_1:
    print(f"The elder is {name_2}")
else:
    print(f"{name_1} and {name_2} are the same age")