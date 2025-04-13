import random
# Define a list of words directly in this file
words = [
    'python', 'programming', 'computer', 'algorithm', 'database',
    'network', 'software', 'hardware', 'internet', 'developer',
    'coding', 'debugging', 'testing', 'deployment', 'version',
    'control', 'repository', 'function', 'variable', 'class'
] 

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    print("Selected word:", word)

hangman()
