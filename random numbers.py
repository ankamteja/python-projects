import random

number = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    guess = input("Guess a number between 1 and 100")
    guess = int(guess)
    if guess == number:
        print("Congrats, You're correct!")
        print(attempts)
        break
    elif guess < number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
