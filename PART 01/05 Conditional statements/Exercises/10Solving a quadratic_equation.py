# Write a program for Solving a quadratic equation of the form ax²+bx+c. 
# The program asks for values ​​a, b and c. 
# It should then use the quadratic formula to solve the equation. 
# The quadratic formula expressed with the Python sqrtfunction is as follows:

# x = (-b ± sqrt(b²-4ac))/(2a).

# You can assume the equation will always have two real roots, so the above formula will always work.

# An example of expected behavior:

#Sample output
#Value of a: 1 
#Value of b: 2 
#Value of c:-8
#The roots are 2.0 and -4.0

a = int(input("#Value of a: "))
b = int(input("#Value of b: "))
c = int(input("#Value of c: "))

D = b*b - 4*a*c

root_1 = (-b + sqrt(D)) / 2*a
root_2 = (-b - sqrt(D)) / 2*a

print(f"he roots are {root_1} and {root_2}")

