import random

#constant variable for the hangman visual
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  o   |
      |
      |
     ===''','''
  +---+
  o   |
  |   |
      |
     ===''','''
  +---+
  o   |
 /|   |
      |
     ===''','''
  +---+
  o   |
 /|\  |
      |
     ===''','''
  +---+
  o   |
 /|\  |
 /    |
     ===''','''
  +---+
  o   |
 /|\  |
 / \  |
     ===''']

# Words for hangman solution
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra' .split()

def getRandomWord(wordList) :
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

# Display board function, to show hangman, correct letters, and missed letters
def displayBoard(missedLetters, correctLetters, secretWord) :
    print(HANGMAN_PICS [len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)) : # Replace blanks with correctly guessed letters
        if secretWord [i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letters.
        print(letter, end=' ')
    print()

