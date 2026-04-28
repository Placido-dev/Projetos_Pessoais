# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Silva',
}

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(chave, valor)
