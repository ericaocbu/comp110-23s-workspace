"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730560123"

secret: str = "python"
guess = str(input("What is your 6-letter guess? "))

count: int = 0
result: str = ""

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")

while count < len(secret):
    if guess[count] == secret[count]:
        result = result + green_box
    else:
        b: bool = False
        s: int = 0
        while ((b is not True) and (s < 6)):
            if (guess[count] == secret[s]):
                b = True
            else:
                s = s + 1
        if (b is True):
            result = result + yellow_box
        else:
            result = result + white_box
    count = count + 1

print(result)

if guess == secret:
    print("Woo ! You got it! ")
else:
    print("Not quite. Play again soon! ")