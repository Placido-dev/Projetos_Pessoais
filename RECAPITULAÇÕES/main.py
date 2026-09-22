# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

lista_repetidos = [
    1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9, 10
]

def contar_repetidos(numeros):
    ja_vistos = set()
    for numero in numeros:
        if numero in ja_vistos:
            print('duplicado', numero)
        else:
            ja_vistos.add(numero)
            print(numero)
    return print(f'Vimos {len(ja_vistos)} valores únicos')         

print(contar_repetidos(lista_repetidos))