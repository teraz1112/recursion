print("Input a minimum number")
min = int(input())
print("Input a maximum number")
max = int(input())
if min > max:
    print("The minimum number is greater than the maximum number")
    # guessTheNumberGame.pyを最初から始めるかどうかを尋ねる
    print("Do you want to try again? (yes or no)")
    answer = input()
    if answer == "yes":
        exec(open("guessTheNumberGame.py").read())
    else:
        print("Goodbye")
else:
    print("Guess a number between " + str(min) + " and " + str(max))
    import random
    number = random.randint(min, max)
    guess = int(input())
    while guess != number:
        if guess < min or guess > max:
            print("The number is not between " + str(min) + " and " + str(max))
        else:
            if guess < number:
                print("Too low")
            else:
                print("Too high")
        guess = int(input())
    print("You guessed the number!")

