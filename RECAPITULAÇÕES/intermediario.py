# INTERMEDIÁRIO

# Listas, dicts, tuplas, conjuntos

notas = [
    0, 0, 0, 0, 0, 0, 0
]

soma = 0
x = 0

while x < 7:
    notas[x] = float(input(f'Nota {x}: '))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f'Nota {x}: {notas[x]:.2f}')
    x += 1    

print(f'Média da soma = {soma / x:.2f}')        


numeros = [
    0, 0, 0, 0, 0
]

x = 0
while x < 5:
    numeros[x] = int(input(f'número {x + 1}: '))
    x += 1
while True:
    escolhido = int(input('Que posição você deseja imprimir (0 para sair): '))
    if escolhido == 0 or escolhido > 5:
        print('Você saiu do loop')
        break
    print(f'Você escolheu o número: {numeros[escolhido - 1]}')

lista_1 = []
lista_2 = []

while True:
    entrada_1 = int(input('Digite um número para adicionar a lista [0 para sair]: '))
    if entrada_1 == 0:
        print(f'Comando {entrada_1} digitado, sua primeira lista ficou: {lista_1}')
        break     

    lista_1.append(entrada_1)
    print(f'Valor adicionado na primeira lista: {lista_1[-1]}.')
    print(lista_1)

while True:
    entrada_2 = int(input('Digite outro número para adicionar na segunda lista: '))
    if entrada_2 == 0:
        print(f'Comando {entrada_2} digitado, sua segunda lista ficou: {lista_2}')
        break

    lista_2.append(entrada_2)
    print(f'Valor adicionado na segunda lista: {lista_2[-1]}.')
    print(lista_2)

lista_3 = lista_1 + lista_2

print(f'Lista 1 = {lista_1}, lista 2 = {lista_2}; lista 3 = {lista_3}')

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







# Funções

numero = 10

def multiplicar(numero, multiplicador): 
    while multiplicador <= 10:
        result = numero * multiplicador
        print(f'Multiplicando {numero} x {multiplicador} = {result}')
        multiplicador += 1

multiplicar(numero, 1)

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