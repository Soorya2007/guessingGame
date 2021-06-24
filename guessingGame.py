import random

print("Hello and welcome , to the Number Guesser Game!")

number = random.randrange(1,9)
guesses = int(1)
guess = int(input("Enter Your Guess Here "))
nxtGuess = int(0)

if(guesses<5):
    guesses=guesses+1

elif(guesses==5):
    print("You Are Out Of Guesses.")
    print("The number was"+str(number))

if(guess==number):
    print("You are correct!Congratulations")

elif(guess==number-3 | guess==number+3):
    print("Ooh that was pretty close . Try Again!                  Guess="+str(guesses))

else:
    print("That guess was pretty far . Try again!                  Guess="+str(guesses))
