import random
from random import choice

def menu():
    print("Let's play heads or tails")
    print("[1] Heads")
    print("[2] Tails")
    print("[3] Exit")

def choice_option(which_will_be, player_choice):
    if player_choice == which_will_be:
        print("WIIIINER!!!")
    else:
        print("LOOOSER!!!")

def main():
    while True:
        menu()
        which_will_be = random.choice(['heads',  'tails'])
        player_choice = input()

        if player_choice == '1':
            player_choice = 'heads'
        elif player_choice == '2':
            player_choice = 'tails'
        elif player_choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3")
            continue
            
        choice_option(which_will_be, player_choice)


if __name__ == "__main__":
    main()



    





