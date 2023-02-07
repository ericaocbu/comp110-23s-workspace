"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730560123"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

user_character: str = input("Enter a single character: ")
if len(user_character) != 1:
    print("Error: Word must contain a single character.")
    exit()

print("Searching for " + user_character + " in " + user_word)


character_count: int = 0

if (user_word[0] == user_character):
    print(user_character + " found at index 0")
    character_count = character_count + 1
if (user_word[1] == user_character):
    print(user_character + " found at index 1")
    character_count = character_count + 1
if (user_word[2] == user_character):
    print(user_character + " found at index 2")
    character_count = character_count + 1
if (user_word[3] == user_character):
    print(user_character + " found at index 3")
    character_count = character_count + 1
if (user_word[4] == user_character):
    print(user_character + " found at index 4")
    character_count = character_count + 1

if (character_count == 0):
    print("No instances of " + user_character + " found in " + user_word)
else:
    if (character_count > 1):
        print(str(character_count) + " instances of " + user_character + " found in " + user_word)
    else:
        print("1 instance of " + user_character + " found in " + user_word)