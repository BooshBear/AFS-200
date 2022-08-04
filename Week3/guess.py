theWord = 'PINEAPPLE'
usrGuesses = []
wordBoard = ['_'] * len(theWord)
tries = 5

def showBoard():
    print(wordBoard)

def checkGuess(theGuess):
    global tries
    if 0 < len(theGuess) > 1:
        print("Sorry you may only use 1 character")
    elif theGuess in usrGuesses:
        print("You have already guessed that character.")
    elif theGuess not in theWord:
        print(f"Sorry the letter {theGuess} is not in the word.")
        tries = tries - 1
        print(f"You have {tries} left.") 
        usrGuesses.append(theGuess)    
    elif theGuess in theWord:
        print(f"Yes the letter {theGuess} is in the word.")
        usrGuesses.append(theGuess)
        indices = [i for i, letter in enumerate(theWord) if letter == theGuess]
        for index in indices:
            wordBoard[index] = theGuess
        

while tries >= 1:
    if '_' not in wordBoard:
        print("congrates you finished the game")
        print(f"The word was {theWord}")
        break

    print(showBoard())
    print(usrGuesses)

    guess = input('Guess a letter: ').upper()

    checkGuess(guess)
