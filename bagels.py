import random

NUM_DIGITS = 3
MAX_GUESS = 10

# Generate the secret number.
def getSecretNum() :
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range (NUM_DIGITS) :
        secretNum += str (numbers[i])
    return secretNum

# Function for clues.
def getClues (guess, secretNum) :
    # Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return 'You got it! Good Job!'
    
    clues = []
    for i in range (len(guess)) :
        if guess[i] == secretNum[i] :
            clues.append('Fermi')
        elif guess [i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'
        
        clues.sort()
        return ' '.join(clues)