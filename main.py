import random

print("Welcome to our number guessing game!")
print("I am thinking of a number between 1 and 100.")


# creating the variable difficulty
difficulty = input("Choose your difficulty 'easy' or 'hard': ").lower()

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

# generating a random number
random_number = random.randint(1,100)

# creating a while loop to run game while the user has attempts
while attempts > 0:
    user_guess = int(input("Make your guess: "))

    if user_guess == random_number:
        print("Congratulations you guessed right!")
    elif user_guess > random_number:
        print("Too high")
    else:
        print("Too low")

    attempts -= 1
    print(f"You have {attempts} remaining.")

if attempts == 0:
    print("Sorry you ran out of attempts you lose 😔")

