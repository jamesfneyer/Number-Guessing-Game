import random

def valid_four_choice(choice1, choice2, choice3, choice4, prompt):
    isValid = False
    while not isValid:
        replay = input(prompt)
        if replay.lower() == choice1 or replay.lower() == choice2 or replay.lower() == choice3 or replay.lower() == choice4:
            isValid = True
            if replay.lower() == choice1 or replay.lower() == choice2:
                return choice1
            else:
                return choice3
        else:
            print("Hey! That wasn't a valid input!")

def get_continue(prompt):
    isValid = False
    while not isValid:
        replay = input(prompt)
        if replay.lower() == "y" or replay.lower() == "yes" or replay.lower() == "n" or replay.lower() == "no":
            isValid = True
            return replay.lower() == "y" or replay.lower() == "yes"
        else:
            print("Hey! That wasn't a valid input!")

play_again = True
who_guesses = input("Who is guessing the number? (computer/humanoid) ")

if who_guesses.lower() == "humanoid" or who_guesses.lower() == "human":
    while play_again:
        turns = 10
        correct_guess = False
        my_number = random.randint(1,100)
       # my_number = 50
        while not correct_guess and turns > 0:
            print("Your turns left is "+str(turns))
            your_guess = input("Enter your guess: ")
            try:
                your_number = int(your_guess)
            except ValueError:
                print("Error! Must be an integer.")
            else:
                if your_number == my_number:
                    print("Dang, you got it! And with "+str(turns)+" left!")
                    correct_guess = True
                else:
                    if your_number > my_number:
                        print("You guessed too high!")
                    else:
                        print("You guessed too low!")
                    turns -= 1
        if correct_guess:
            play_again = get_continue("Good job! Would you like to play again? ")
        else:
            play_again = get_continue("You lost! The number I was thinking of was "+str(my_number)+". Would you like to play again?")


elif who_guesses.lower() == "computer":
    while play_again:
        turns = 0
        difference = 50
        guess = 50
        correct_guess = False
        while not correct_guess:
            if turns == 0:
                print("Pick a number between 1 and 100!")
            is_correct = valid_four_choice("yes","y","no","n","Is the number you're thinking of "+str(guess)+"?")
            if is_correct.lower() == "yes":
                replay = input("All too easy. Only took me "+str(turns)+" turns. Play again? ")
                correct_guess = True
                play_again = get_continue("Would you like to play again? ")
            elif is_correct.lower() == "no":
                if difference != 1:
                    difference //= 2
                high_or_low = valid_four_choice("higher","high","lower","low","Dang! Was I too high or low? ")
                if high_or_low.lower() == "higher":
                    guess -= difference
                    correct_hl = True
                    ++turns
                elif high_or_low.lower() == "lower":
                    guess += difference
                    correct_hl = True
                    ++turns