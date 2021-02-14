import random
from art import logo


def start_game():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    comp = [cards[random.randint(0,len(cards))], cards[random.randint(0,len(cards))]]
    user = [cards[random.randint(0,len(cards))], cards[random.randint(0,len(cards))]]
    flag = True
    sum_comp = sum(comp)
    sum_user = sum(user)

    print(logo)
    print(f"    Your cards are: {user}, current score: {sum_user}")
    print(f"    Computer's first card: {comp[0]}")

    while flag:
        
        if sum_user > 21:
            print("You went over. You lose")
            break
        
        continue_game = input("Type 'y' to get another card, type 'n' to pass : ")


        if continue_game == "y" or continue_game == "Y":
            comp.append(cards[random.randint(0,len(cards))])
            user.append(cards[random.randint(0,len(cards))])
            sum_comp = sum(comp)
            sum_user = sum(user)
            print(f"    Your cards are: {user}, current score: {sum_user}")
            print(f"    Computer's first card: {comp[0]}")
            continue

        
        else:
            print(f"    Your final hand: {user}, current score: {sum_user}")
            print(f"    Computer's final hand: {comp}, current score: {sum_comp}")
            if (sum_user > sum_comp) or (sum_comp > 21):
                print("You won!")
            else:
                print("You lose!")
            break
while True:
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if play_game == "y" or play_game == "Y":
        start_game()
        continue
    else:
        break
