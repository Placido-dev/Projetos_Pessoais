# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

numero = 10

def multiplicar(numero, multiplicador): 
    while multiplicador <= 10:
        result = numero * multiplicador
        print(f'Multiplicando {numero} x {multiplicador} = {result}')
        multiplicador += 1

multiplicar(numero, 1)