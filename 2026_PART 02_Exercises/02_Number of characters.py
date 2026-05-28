# The function lencan be used to find out the length of a string, among other things. 
# The function Returns the number of characters in a string.

# Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

word = input("Please type in a word:")
if len(word) > 1:
    print(f"There {len(word)} are letters in the word {word} Thank you!")
print("Thank you!")