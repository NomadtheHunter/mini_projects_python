secret_word = "Zoiao"
guess = ""
while guess != secret_word:
    guess = input("Guess a letter: ")

    if guess == secret_word:
        print("Correct!")
        break
    elif guess in secret_word:
        print("These letters are in the word!")
    else:
        print("Sorry, try again!")