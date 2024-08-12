import random

def get_random_word():
    # List of words for the game
    words = ["python", "hangman", "programming", "challenge", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    # Initialize game variables
    word = get_random_word()
    guessed_letters = set()
    attempts_remaining = 6
    
    print("Welcome to Hangman!")
    
    while attempts_remaining > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts_remaining -= 1
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
