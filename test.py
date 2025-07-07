import random

# Word list
words = ["python", "banana", "coding", "hangman", "school"]
word = random.choice(words)

# Game state
guessed = []
tries = 6

# Display word with underscores
def display_word():
    return " ".join([letter if letter in guessed else "_" for letter in word])