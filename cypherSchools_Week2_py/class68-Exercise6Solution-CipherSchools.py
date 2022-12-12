winning_number = 43
guess = 1
number = input("Guess a number between 1 and 100: ")
game_over = False

while not game_over:
    if number==winning_number:
        print("you win, and you guesses this number in {guess} times")
        game_over = True
        #win
    else:
        if number <winning_number:
            print("too low")
            guess+=1
            number=int(input("guess again: "))
        else:
            print("too high")
            guess+=1
            number=int(input("guess again: "))
        #guess wrong