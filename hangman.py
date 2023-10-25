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