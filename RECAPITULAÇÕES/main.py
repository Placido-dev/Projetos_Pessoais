# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

numero = int(input('Digite um número [inteiro] para duplicar, triplicar e quadruplicar: '))

def multiplicar(numero, multiplicador): 
    result = numero * multiplicador
    if multiplicador == 2:
        print(f'Duplicando: {numero} -> {result}')
    elif multiplicador == 3:
        print(f'Triplicando: {numero} -> {result}')
    elif multiplicador == 4:
        print(f'Quadruplicando: {numero} -> {result}')

multiplicar(numero, 2)
multiplicar(numero, 3)
multiplicar(numero, 4)