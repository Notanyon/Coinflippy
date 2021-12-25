
import random

print("© COPYRIGHT BY TEAM ZAY, NOTANYONE, UNDERSCORE, CALMING WAVES.")


# maximum = the max the user can bet
def ask_wager(total):
    # loops around until user gives a valid amount
    while True:
        response_to_bet = input("How much would you like to bet:  ")

        try:
            amount = int(response_to_bet)
        except ValueError:
            print('this is not integer please input a number')
            continue

        if amount > total:
            print(f"Sorry that is too much you only have {total}")
            continue

        return amount


# just the instructions
def print_instruction():
    name = input("What should I call you: ")

    print(f'Hello {name} you will be starting with 1,000 coins...your goal is to reach Tier 10!')
    print('press ENTER to continue')
    input()

    print('Rules to the game.. you will bet X amount of coins each turn and choose either Heads or Tails..')
    print('if your choice is correct then you will gain the amount of coins you bet. if your choice is incorrect')
    print('you will lose the amount of coins you bet on that turn..Each new tier is at + 10,000 coins')
    print('Good luck!')
    print('press ENTER to continue')
    input()


# coin = [H , T] these are all the coins possible
def ask_cf_choice(coin):
    while True:
        answer = input("Choose Heads or Tails (write [H] for Heads or [T] for tails.): ").upper()

        if answer in coin:
            return answer
        print('Please read carefully!!')


def get_tier(money):
    tier = money // 10000
    return tier


# this is the main code combining all of the code
def main():
    user_money = 1000
    coin = ["H", "T"]
    print_instruction()

    # this while loop is for each round of coin-flip
    while True:
        # this code ask what the user's wager is
        wager = ask_wager(total=user_money)

        # this code ask the user's cf choice
        answer = ask_cf_choice(coin=coin)

        # this code randomly picks the coin
        selection = random.choice(coin)

        # this code will calculate the users tier *before the round*
        old_tier = get_tier(user_money)

        if answer == selection:
            user_money += wager
            print(f"That's correct! your total is {user_money}")
        else:
            user_money -= wager
            print(f"That's incorrect! your total is {user_money}")

        # this code will calculate the users tier *after the round*
        new_tier = get_tier(user_money)

        if new_tier > old_tier:
            print(f'Congrats you have reached tier {new_tier}!')
        elif new_tier < old_tier:
            print(f'LOL YOU SUCK (jp) your new tier is {new_tier}')

        if user_money == 0:
            ask_play_again()


# play again statement
def ask_play_again():
    while True:
        play_again = input(" Your coins are 0 Would you like start over[S] or end the game[E]? [S] or [E]: ").upper()
        if play_again == "S":
            main()
        else:
            print('Hope you enjoyed the game bye!')
            print('press ENTER too continue')
            input()
            exit()


main()