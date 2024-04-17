import random

def roll_dice():
    return random.randint(1, 6)

def print_dice_sum(dice_1, dice_2):
    print("The sum of dice is {} + {} = {}".format(dice_1, dice_2, dice_1 + dice_2))

def play_game():
    dice_1 = roll_dice()
    dice_2 = roll_dice()

    if (dice_1 + dice_2 == 7) or (dice_1 + dice_2 == 11):
        print_dice_sum(dice_1, dice_2)
        print("You won")
    elif (dice_1 + dice_2 == 2) or (dice_1 + dice_2 == 3) or (dice_1 + dice_2 == 12):
        print_dice_sum(dice_1, dice_2)
        print("Casino won")
    else:
        print_dice_sum(dice_1, dice_2)
        print("Now your goal number is : " + str(dice_1 + dice_2))

        while True:
            dice_3 = roll_dice()
            dice_4 = roll_dice()
            print("The sum of dice is {} + {} = {}".format(dice_3, dice_4, dice_3 + dice_4))

            if (dice_3 + dice_4 == dice_1 + dice_2):
                print("You won")
                break
            elif (dice_3 + dice_4 == 7):
                print("You lose")
                break

play_game()

