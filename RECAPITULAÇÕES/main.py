# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

def maior_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

result = maior_de_tres(a=5,b=5,c=3)
print(result)