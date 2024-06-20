import random
from random import choice #escolha um item em uma lista

# num_between_zero_one = random.random() #gera uma valor entre 0 e 1
# print(num_between_zero_one)

# random_num_decimal_of_equal_probability = random.uniform(10, 100) #gera valores aleatorios decimais entre os valores estipulados
# print(random_num_decimal_of_equal_probability)

# random_num_int_of_equal_probability = random.randint(10, 999) #gera valores inteiros de igual probabilidade entre os valores estipulados
# print(random_num_int_of_equal_probability)

# value_distribution_normal = random.gauss(10, 30)
# print(value_distribution_normal)

# tickers = ['WEGE3', 'PCAR3', 'LREN3']
# company_chosen = choice(tickers)
# print(company_chosen)

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



    





