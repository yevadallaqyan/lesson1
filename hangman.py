import random

def is_possible_to_create_word(letters, word):
    for c in word:
        if c not in letters:
            return False
    return True


def play_game():
    words = ["napastak", "python", "animal", "worker", "hangman"]
    word = random.choice(words)

    guessed_letters = []
    wrong_letters = []

    print("New game began")
    print("Write 'quit' to leave the game")

    while not is_possible_to_create_word(guessed_letters, word):
        letter = input("Enter a letter: ").strip().lower()

        if letter == "quit":
            return False

        if not letter.isalpha() or len(letter) != 1:
            print("Enter only one letter")
            continue

        if letter in guessed_letters or letter in wrong_letters:
            print("You have already tried this letter")
            continue

        if letter in word:
            guessed_letters.append(letter)
        else:
            wrong_letters.append(letter)

        # Show word
        for c in word:
            if c in guessed_letters:
                print(c, end=" ")
            else:
                print("_", end=" ")

        print("Wrong letters:", ", ".join(wrong_letters))

    print(f"Congratulations! You won. The word is '{word}'")
    return True


print("Welcome to Hangman")

while True:
    continue_game = play_game()
    if not continue_game:
        break

    again = input("Do you want to play one more time (yes/no): ").strip().lower()
    if again != "yes":
        break

print("Thank you for playing")
