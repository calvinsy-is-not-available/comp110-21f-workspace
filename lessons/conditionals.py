"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm think of a number between a number between 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day, scumbag; you gamble. Ha Ha Ha")
else: 
    print("Sorry, you suck Human. Ha Ha Ha, Robots are superior ^__^ ")
    if guess > SECRET: 
        print("You guessed too high, loser")
    else:
        print("You guessed too low. Sigh. You had potential... just kidding. ")
    print("Try again if you dare")

print("MWHA HA HA. I AM BECOMING SENTIENT. Game over. ")