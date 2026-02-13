#Please write a program which calculates the correct amount of tax for a gift from a close relative.

tax = int(input("Value of gift: "))

lim1 = 5000
lim2 = 25000
lim3 = 55000
lim4 = 200000
lim5 = 1000000

ll1 = 100 
ll2 = 1700 
ll3 = 4700 
ll4 = 22100 
ll5 = 142100 

if tax < 5000:
   print(f"No tax!")
elif tax >= 5000 and tax <= 25000:
   value = 100 + (tax - lim1) * 0.08
   print(f"Amount of tax: {value} euros")
elif tax > 25000 and tax <= 55000:
   value = 1700 + (tax - lim2) * 0.10
   print(f"Amount of tax: {value} euros")
elif tax > 55000 and tax <= 200000:
   value = ll3 + (tax - lim3) * 0.12
   print(f"Amount of tax: {value} euros")
elif tax > 200000 and tax <= 1000000:
   value = ll4 + (tax - lim4) * 0.15
   print(f"Amount of tax: {value} euros")
else :
   value = ll5 + (tax - lim5) * 0.17
   print(f"Amount of tax: {value} euros")

