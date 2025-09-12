# Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

word = input("Please type in a word: ")

length = len(word)

if length > 1:
   print(f"There are {length} letters in the word {word}")
   
print(f"Thank you!")