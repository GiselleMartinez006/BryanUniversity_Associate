# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: 
# one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

a = int(input("Give me a number and i'll tell you if it is even or odd! "))
if a % 4 == 0: 
      print("not just is it even, it is a multiple of 4!")
elif a % 2 == 0:
  print("even")
else:
  print("odd")


# extra: 
def game():
    def runningGame():
        num1 = int(input("Give me a number num1! "))
        num2 = int(input("Give me a number num2! "))
        remainder = num1 % num2 
        if num1 == num2: 
            print("They are the same number!")
        elif remainder == 0:
            print("They divide evenly! Congrats!")
        else:
            print(f"D: they don't divide evenly. It has a remainder of {remainder}.")
    def playingAgain():
        again = input("Want to play again? yes/y/yep OR nop/no/n : " )
        if again == "yes" or again== "y" or again ==  "yep":
            runningGame()
            playingAgain()
    extraGame = input("Let's play! Give me two numbers: I'll divide them for you and tell you if num1 is divisible by num2! Ready? y/yes OR n/no OR 'I dont want to play'/'I don't want to play': ")
    if extraGame == "y" or extraGame == "yes":
        print("yes")
        runningGame()
        playingAgain()    
    elif extraGame == "no" or extraGame == "n":
        askingAgain = input("Ready now? y/yes OR n/no OR 'I dont want to play'/'I don't want to play': ")
        if askingAgain == "y" or askingAgain == "yes":
            print("yes")
            runningGame()
            playingAgain()
        elif askingAgain == "n" or askingAgain == "no":
            print(askingAgain)
            game()
        else:
            print("bye!")
    else:
        print("bye!")

game()

