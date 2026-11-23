# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

numero = int(input())
hrs_trabalhadas = int(input())
valor_hr = float(input())

salario = hrs_trabalhadas * valor_hr
print(f'NUMBER = {numero}')
print(f'SALARY = U$ {salario:.2f}')