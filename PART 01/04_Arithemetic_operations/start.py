# In the previous sections you've seen examples with basic arithmetics. In the following table you can see the most common arithmetic operators in Python, with examples:

#nOperator	Purpose	Example	Result
# +	Addition	2 + 4	6
# -	Subtraction	10 - 2.5	7.5
# *	Multiplication	-2 * 123	-246
# /	Division (floating point result)	9 / 2	4.5
# //	Division (integer result)	9 // 2	4
# %	Modulo	9 % 2	1
# **	Exponentiation	2 ** 3	8

#The order of operations is familiar from mathematics: first calculate the exponents, then multiplication and division, and finally addition and subtraction. The order can be changed with parentheses.

# For example this bit of code

print(2 + 3 * 3)
print((2 + 3) * 3)

# prints out

11
15