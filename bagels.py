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

