import random

def load_words(filename):
    """Read words from a file and return them as a list."""
    words = []
    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            if word:  # skip empty lines
                words.append(word.upper())
    return words

def display_word(secret_word, guessed_letters):
    """Show the word with correctly guessed letters revealed, dashes for the rest."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def play_game(secret_word, max_guesses=8):
    """Run one round of the word guessing game."""
    guessed_letters = []
    guesses_left = max_guesses

    print("\n--- NEW GAME ---")
    print(f"The secret word has {len(secret_word)} letters.\n")

    while guesses_left > 0:
        current_display = display_word(secret_word, guessed_letters)

        # Check if the player has won
        if current_display == secret_word:
            print(f"The word now looks like this: {current_display}")
            print("\nYou guessed the word! You win! 🎉")
            return True

        print(f"The word now looks like this: {current_display}")
        print(f"You have {guesses_left} guesses left")

        if guessed_letters:
            print(f"Letters guessed so far: {', '.join(sorted(guessed_letters))}")

        guess = input("Type a single letter here, then press enter: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("That guess is correct.\n")
        else:
            guesses_left -= 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # Player ran out of guesses
    print(f"\nOut of guesses! The secret word was: {secret_word}")
    return False

def main():
    print("=== WORD GUESSING GAME ===")

    # Load words from file
    try:
        word_list = load_words("words.txt")
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Make sure it's in the same folder.")
        return

    wins = 0
    games = 0

    while True:
        secret_word = random.choice(word_list)
        result = play_game(secret_word)

        games += 1
        if result:
            wins += 1

        print(f"\nScore: {wins} win(s) out of {games} game(s)")
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye.")
            break

main()
