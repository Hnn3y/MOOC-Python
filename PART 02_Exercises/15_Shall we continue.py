# This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". 
# Then the program should print out "okay then" and finish. 
# Please have a look at the example below.


while True:
   print(f"hi")
   ans = input(f"Shall we continue?")
   if ans == "no":
      break

print(f"okay then")


