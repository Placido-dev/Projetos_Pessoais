# Listas, dicts, tuplas, conjuntos

lista_1 = [1, 2, 3, 2]
lista_2 = [2, 3, 4, 5]
lista_3 = []

x = 0

while x < len(lista_1) or x < len(lista_2):
    if x < len(lista_1):
        if lista_1[x] not in lista_3:
            lista_3.append(lista_1[x])
    if x < len(lista_2): 
        if lista_2[x] not in lista_3:
            lista_3.append(lista_2[x])
    x += 1

print(lista_3)