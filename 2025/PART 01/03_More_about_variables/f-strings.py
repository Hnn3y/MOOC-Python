#  f-strings are another way of formatting printouts in Python.

# With f-strings the previous example would look like this:

result = 10 * 25
print(f"The result is {result}")

# The value it contains becomes a part of the printed string.

# A single f-string can contain multiple variables.
name = "Mark"
age = 37
city = "Palo Alto"
print(f"Hi {name}, you are {age} years old. You live in {city}.")

# It is difficult to create a printout exactly like this using the comma notation in the print command.
name = "Mark"
age = 37
city = "Palo Alto"
print("Hi", name, ", you are", age, "years old. You live in", city, ".")
# prints out the following:

# Sample output
# Hi Mark, you are 37 years old. You live in Palo Alto.