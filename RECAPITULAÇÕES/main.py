# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Silva',
    'idade': '24',
    'altura': '1.7',
    'enderecos': [
        {'rua': 'segredo', 'numero': 10},
        {'rua': 'outra', 'numero': 5},
    ],
}

for i in pessoa:
    print(i, pessoa[i])
