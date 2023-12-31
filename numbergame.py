# This is a Guess the Number game.
import random

# Assigns the variable for guesses
guessesTaken = 0

# Variable for players name and greeting
print('Hello! What is your name?')
myName = input()

# Random number variable
number = random.randint(1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

# Tells you if you're high or low relevant to your answer.
for guessesTaken in range(10):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Oops, your guess is too low!')

    if guess > number:
        print('Yikes! Your number is too high!')

    if guess == number:
        break

# Game results
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + ' you guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')