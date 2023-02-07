
"""Ask user for a number"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True
number_of_guesses: int = 0

while playing:
    if guess == SECRET:
        print("Yay! You got it right. ")
        playing = False
    else:
        print("Wrong number. :( ")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd, the answer is even.")
        if guess > SECRET:
            print("Your guess is too high! ")
        else: #guess < secret
            print("Your guess is too low. ")
        guess = int(input("Male another guess!"))
number_of_guess = number_of_guesses + 1
print("Number of guesses " + str(number_of_guesses))
