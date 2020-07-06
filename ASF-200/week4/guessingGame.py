import random
number = random.randint(1,9)
# print(number, "random number- testing only")
 
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
       
    elif int(userInputNum) == num: 
        print(num)
        # print("length",attempts.__len__()) 
        if attempts.__len__() == 0:
            print("WOW! You got it on the first try!")
        else: 
            print("Congrats! You got it! Attempts before right answer: ", attempts)
        playAgain()
    elif int(userInputNum) > num: 
        print(f'Good try! However, {userInputNum} is BIGGER than the number. Try Again!')
        attempts.append(userInputNum)
        guessingGame(attempts, num)
    elif int(userInputNum) < num: 
        print(f'Good try! However, {userInputNum} is SMALLER than the number. Try Again!')
        attempts.append(userInputNum)
        guessingGame(attempts, num)
    
guessingGame([], number)
