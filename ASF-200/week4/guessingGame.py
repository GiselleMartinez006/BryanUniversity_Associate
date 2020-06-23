import random
# Generate a random number between 1 and 9 (including 1 and 9).
#  Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# To use a module, at the top of your file, type

#      import random

# This means you are allowing your Python program to use a module called random in the rest of your code.

# To use it (and generate a random integer), now type:


# w = 0
# while w < 20:
number = random.randint(1,9)
print(number, "random number- testing only")
    # w=w+1

def guessingGame(attempts=[], num = number):
    def playAgain():
            askagain = input("would you like to play again? Say y for yes or n for no! ")
            if askagain == 'y': 
                newA = random.randint(1,9)
                guessingGame([], newA)
            else: 
                print("Bye!")
    userInputNum = input("Let's play a game! Guess what number I have! -or type 'exit' to leave- ")
    if str(userInputNum) == "exit": 
        print(f'User is leaving! Bye! -The number was {num} btw')
        playAgain()
    elif int(userInputNum) == num: 
        print(num)
        # print("length",attempts.__len__()) 
        if attempts.__len__() == 0:
            print("WOW! You got it on the first try!")
        else: 
            print("Congrats! You got it! Attempts before right answer: ", attempts)
        playAgain()
    elif int(userInputNum) > num: 
        print(f'Good try! However, {userInputNum} is is BIGGER than the number. Try Again!')
        attempts.append(userInputNum)
        guessingGame(attempts, num)
    elif int(userInputNum) < num: 
        print(f'Good try! However, {userInputNum} is is SMALLER than the number. Try Again!')
        attempts.append(userInputNum)
        guessingGame(attempts, num)
    
guessingGame([], number)
