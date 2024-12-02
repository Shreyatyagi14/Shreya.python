import random

# Word list with hints
words_with_hints = [
    ("python", "A popular programming language"),
    ("elephant", "The largest land animal"),
    ("guitar", "A musical instrument with strings"),
    ("sunflower", "A bright yellow flower that follows the sun"),
    ("mountain", "A large natural elevation of the earth's surface")
]

# Hangman visuals
hangman_visuals = [
    """
     -----
     |   |
         |
         |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    """
]

def hangman():
    # Randomly select a word and hint
    word, hint = random.choice(words_with_hints)
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    attempts = 0
    max_attempts = len(hangman_visuals) - 1

    print("Welcome to Hangman!")
    print("Hint:", hint)
    print(" ".join(guessed_word))
    
    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            for idx, char in enumerate(word):
                if char == guess:
                    guessed_word[idx] = char
        else:
            print("Incorrect!")
            attempts += 1

        print(hangman_visuals[attempts])
        print("Guessed word:", " ".join(guessed_word))

        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("You've run out of attempts! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
