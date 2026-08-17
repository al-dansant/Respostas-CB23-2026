import time
from AP_03_ordenacao import selection_sort
from AP_03_ordenacao import divide_and_conquer_sort
from AP_03_ordenacao import quick_sort
import random
import sys

sys.setrecursionlimit(max(10000, 6000))

random.seed(1001)

def random_list(n):

    "Cria uma lista com n números distintos organizados aleatóriamente"

    list = []
    for i in range(1, n + 1): # Cria uma lista ordenada
        list.append(i)
    random.shuffle(list) # Organiza a lista de forma aleatória
    return list

def inverse_order_list(n):

    "Cria uma lista inversamente ordenada"

    list = []
    for i in range(1, n + 1):
        list.append(n + 1 - i) # Adição de números na ordem decrescente
    return list
 
rep = 50 # Repetições

"Criação da tabela de apresentação dos dados"

table = []    
table.append(["-----------------------------------------------------------"])
table.append(["|Algorítmo               |  Cenário   |  N  | Tempo Médio |"]) 
table.append(["-----------------------------------------------------------"])

for n in [100, 500, 1000, 5000]:

    '---------------------------------'
    "Testes com lista aleatória"
    '---------------------------------'

    rand_list = random_list(n) # Criação de uma lista ordenada aleatóriamente

    "selection_sort"

    time_1 = []
    for i in range(1, rep + 1):
        inicio = time.perf_counter()
        selection_sort(rand_list)
        fim = time.perf_counter()
        t = fim - inicio
        time_1.append(t)
    t_medio_random_alg1 = sum(time_1)/len(time_1)

    "divide_and_conquer_sort"

    time_2 = []
    for i in range(1, rep + 1):
        inicio = time.perf_counter()
        divide_and_conquer_sort(rand_list)
        fim = time.perf_counter()
        t = fim - inicio
        time_2.append(t)
    t_medio_random_alg2 = sum(time_2)/len(time_2)    

    "quick_sort"

    time_3 = []
    for i in range(1, rep + 1):
        inicio = time.perf_counter()
        quick_sort(rand_list)
        fim = time.perf_counter()
        t = fim - inicio
        time_3.append(t)
    t_medio_random_alg3 = sum(time_3)/len(time_3)

    '-----------------------------------------------'
    "Testes com lista ordenada inversamente"
    '-----------------------------------------------'

    inverse_list = inverse_order_list(n) # Criação de uma lista inversamente ordenada

    "selection_sort"

    time_1 = []
    for i in range(1, rep + 1):
        inicio = time.perf_counter()
        selection_sort(inverse_list)
        fim = time.perf_counter()
        t = fim - inicio
        time_1.append(t)
    t_medio_inverse_alg1 = sum(time_1)/len(time_1)

    "divide_and_conquer_sort"

    time_2 = []
    for i in range(1, rep + 1):
        inicio = time.perf_counter()
        divide_and_conquer_sort(inverse_list)
        fim = time.perf_counter()
        t = fim - inicio
        time_2.append(t)
    t_medio_inverse_alg2 = sum(time_2)/len(time_2)    

    "quick_sort"

    time_3 = []
    for i in range(1, rep + 1):
        inicio = time.perf_counter()
        quick_sort(inverse_list)
        fim = time.perf_counter()
        t = fim - inicio
        time_3.append(t)
    t_medio_inverse_alg3 = sum(time_3)/len(time_3)

    "Adição dos resultados na tabela"

    table.append([f"|selection_sort          | caso médio | {n} |  {t_medio_random_alg1:.6f}   |"])
    table.append([f"|divide_and_conquer_sort | caso médio | {n} |  {t_medio_random_alg2:.6f}   |"])
    table.append([f"|quick_sort              | caso médio | {n} |  {t_medio_random_alg3:.6f}   |"])
    table.append(["-----------------------------------------------------------"])
    table.append([f"|selection_sort          | pior caso  | {n} |  {t_medio_inverse_alg1:.6f}   |"])
    table.append([f"|divide_and_conquer_sort | pior caso  | {n} |  {t_medio_inverse_alg2:.6f}   |"])
    table.append([f"|quick_sort              | pior caso  | {n} |  {t_medio_inverse_alg3:.6f}   |"])
    table.append(["-----------------------------------------------------------"])

"Apresentação da tabela"

for line in table:
    print(line[0])