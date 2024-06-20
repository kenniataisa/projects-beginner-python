import random
from random import choice #escolha um item em uma lista

num_between_zero_one = random.random() #gera uma valor entre 0 e 1
print(num_between_zero_one)

random_num_decimal_of_equal_probability = random.uniform(10, 100) #gera valores aleatorios decimais entre os valores estipulados
print(random_num_decimal_of_equal_probability)

random_num_int_of_equal_probability = random.randint(10, 999) #gera valores inteiros de igual probabilidade entre os valores estipulados
print(random_num_int_of_equal_probability)

value_distribution_normal = random.gauss(10, 30)
print(value_distribution_normal)

tickers = ['WEGE3', 'PCAR3', 'LREN3']
company_chosen = choice(tickers)
print(company_chosen)
