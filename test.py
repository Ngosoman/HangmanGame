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

print("Welcome to Hangman!")
print(display_word())

# Game loop
while tries > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print(" Correct!")
    else:
        guessed.append(guess)
        tries -= 1
        print(" Wrong! You have", tries, "tries left.")

    print(display_word())

    # Win check
    if all(letter in guessed for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Lose check
if tries == 0:
    print("💀 Game Over! The word was:", word)