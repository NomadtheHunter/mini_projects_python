secret_word = "Cinos"
guess = ""
guess_count = 0
guess_limit = 5

print("""Welcome to the secret word Game
You got 5 tries to guess the word!""")

while guess != secret_word:
    guess = input("Guess a letter: ")
    guess_count += 1

    if guess == secret_word:
        print("Correct!")
        break

    if guess_count >= guess_limit:
        print(f"Game over! The word was {secret_word}")
        break
    elif guess in secret_word:
        print("This letter is in the word!")
    else:
        print("Sorry, try again!")

    print(f"Attempts left: {guess_limit - guess_count}")

    if guess_count == 1:
        print("Hint: Famous video game character.")
    if guess_count == 4:
        print("Hint: My favorite character in games since I was 4, spelled backwards.")