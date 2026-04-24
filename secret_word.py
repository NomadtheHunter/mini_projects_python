secret_word = "Zoiao"
guess = ""
while guess != secret_word:
    guess = input("Guess a letter: ")
    if guess == secret_word:
        print("Congratulations! You guessed the word!")
        break
    else:
        print("Sorry, try again!")