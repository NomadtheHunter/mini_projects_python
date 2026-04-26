secret_word = "Zoiao"
guess = ""
guess_count = 0
guess_limit = 3

print("""Welcome to the secret word Game
You got 3 tries to guess the word!""")

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

    if guess_count == 2:
        print("Hint: Nick name I had when I was a kid")