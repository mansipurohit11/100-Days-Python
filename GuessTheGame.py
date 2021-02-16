import random
from art import logo

print(logo)
print("Welcome to gussing game!\nI'm thinking of a number between 1 to 100.")
type = input("Choose a difficulty. Type 'easy' or 'hard': ")

answer = random.randint(1, 100)
if type == "easy":
    chances = 10
elif type == "hard":
    chances = 5
else:
    print("Sorry wrong input try again")

game_over = True
while game_over:
    print(f"You have {chances} attemps remaining to guess the number")
    choice = int(input("Make a guess: "))
    if choice == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif chances == 1:
        print("You run out of guesses, you loss.")
        break
    else:
        if choice > answer:
            print("Too high")
        elif choice < answer:
            print("Too low")
        chances -= 1
        continue