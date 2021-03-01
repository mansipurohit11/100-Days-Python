import random
from HigherLowerGamedata import data
from art import logo, vs

def check_ans(guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"

def game():
    start_game = True
    score = 0
    x = random.randint(0, len(data))

    while start_game:

        name_a = data[x]["name"]
        country_a = data[x]["country"]
        description_a = data[x]["description"]
        follower_count_a = data[x]["follower_count"]
        print(f"Compare A: {name_a}, {description_a}, from {country_a}")

        print(vs)
        y = random.randint(0, len(data))
        name_b = data[y]["name"]
        country_b = data[y]["country"]
        description_b = data[y]["description"]
        follower_count_b = data[y]["follower_count"]
        print(f"Against B: {name_b}, {description_b}, from {country_b}")


        user_ans = input("Who has more followers? Type 'A' or 'B': ")

        is_correct = check_ans(user_ans, follower_count_a, follower_count_b)

        print(logo)
        if is_correct:
            score += 1
            print(f"You are right! Your current score is {score}.")
        else:
            start_game = False
            print(f"Sorry, that's wrong. Your final score {score}")
        x = y

game()