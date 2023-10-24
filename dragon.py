import random
import time

# Function to display intro to game
def displayIntro():
    print('''You are in a land full of dragons. In front of you, 
          you see two caves. In one cave, the dragon is friendly 
          and will share his treasure with you. The other dragon 
          is greedy and hungry, and will eat you on sight.''')
    print()

# function for cave input
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave 

# function for set-up dialogue for cave choice
def checkCave (chosenCave) :
    print('You approach the cave...')
    time.sleep(2) # sleep function for a temp pause
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    # random int function to set one result to the friendly cave.
    friendlyCave = random.randit(1, 2)

    # If, else function to display result depending on if it was the correct guess.
    if chosenCave == str(friendlyCave) :
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

# Function to ask player if they'd like to play again
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()