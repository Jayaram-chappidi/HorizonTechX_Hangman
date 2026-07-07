import random

# List of predefined words
words = ["python", "apple", "computer", "banana", "school"]

# Randomly select a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
wrong_attempts = 0

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_attempts < max_attempts:
    # Display the current progress of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts left:", max_attempts - wrong_attempts)

    # Check if the player has guessed the whole word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        wrong_attempts += 1
        print("❌ Wrong guess!")

# If attempts are exhausted
if wrong_attempts == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)