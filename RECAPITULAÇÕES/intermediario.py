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

def somar(a, b):
    return a + b

resultado = somar(3, 5)
print(resultado)  # 8

def eh_par(numero):       # recebe por parâmetro
    return numero % 2 == 0  # retorna True ou False

print(eh_par(4))  # True
print(eh_par(7))  # False

def calcular_imc(peso, altura):
    return peso / altura ** 2

imc = calcular_imc(70, 1.70)
print(f'{imc:.2f}')

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    if imc < 18.5:
        return imc, "Abaixo do peso"
    elif imc < 25:
        return imc, "Peso normal"
    elif imc < 30:
        return imc, "Sobrepeso"
    else:
        return imc, "Obesidade"

imc, classificacao = calcular_imc(70, 1.70)
print(f'IMC: {imc:.2f} — {classificacao}')

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


"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def achar_duplicado(numeros):
    numeros_vistos = set()    
    for numero in numeros:
        if numero in numeros_vistos:
            print('duplicado', numero)
            return numero
        else:
            numeros_vistos.add(numero)
            print('adicionando o', numero)
    return -1

print(achar_duplicado(lista_de_listas_de_inteiros[1]))

for i in range(6):
    for j in range(6):
        if (i + j) % 2 == 0:
            print('.', end='')
        else:
            print('#', end='')
    print()