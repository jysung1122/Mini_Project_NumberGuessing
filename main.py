import art
import random

NUMBER = random.randint(1, 100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(answer, attempts):
    if NUMBER > answer:
        print("Too low.")
        attempts -= 1
        return attempts
    elif NUMBER < answer:
        print("Too high.")
        attempts -= 1
        return attempts
    elif NUMBER == answer:
        print(f"You got it! The answer was {NUMBER}.")
        attempts = -1
        return attempts


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS


def game():
    print(art.logo)
    print(f"Answer : {NUMBER}")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))

        attempts = check_answer(answer, attempts)

        if attempts == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again")

game()