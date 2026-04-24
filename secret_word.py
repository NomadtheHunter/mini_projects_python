secret_word = "Zoiao"
guess = ""
while guess != secret_word:
    guess = input("Guess a letter: ")
    if guess in secret_word:
        print("This letter is in the word")
    elif guess in secret_word:
        print("Congratulations! You guessed the word!")
        break
    else:
        print("Sorry, try again!")