# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

# peso / altura * altura

def calcular_imc(peso, altura):
    return peso / altura ** 2

imc = calcular_imc(70, 1.70)
print(f'{imc:.2f}')