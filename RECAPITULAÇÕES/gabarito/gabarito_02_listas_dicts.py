# GABARITO 02 - LISTAS, TUPLAS, DICTS, CONJUNTOS
# Tente resolver sozinho antes de olhar aqui!

# 1) Lista de notas
notas = []
x = 0
while x < 5:
    notas.append(float(input(f'Nota {x + 1}: ')))
    x += 1

# sem max/min
maior = notas[0]
menor = notas[0]
for n in notas:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'Maior: {maior} | Menor: {menor} | Média: {sum(notas)/len(notas):.2f}')
# com max/min
print(f'Maior: {max(notas)} | Menor: {min(notas)}')


# 2) Lista sem repetidos, mantendo ordem
numeros = [4, 5, 4, 2, 7, 5, 9, 2, 1, 4]
sem_repetidos = []
for n in numeros:
    if n not in sem_repetidos:
        sem_repetidos.append(n)
print(sem_repetidos)  # [4, 5, 2, 7, 9, 1]


# 3) Contagem de palavras
frase = "o rato roeu a roupa do rei de roma o rato"
contagem = {}
for palavra in frase.lower().split():
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)


# 4) Inverter um dicionário
capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
}
invertido = {}
for pais, capital in capitais.items():
    invertido[capital] = pais
print(invertido)
# ou, de forma mais enxuta: invertido = {v: k for k, v in capitais.items()}


# 5) Interseção e diferença com sets
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]
set_a = set(lista_a)
set_b = set(lista_b)
print('Em comum:', set_a & set_b)        # {4, 5, 6}
print('Só em a:', set_a - set_b)         # {1, 2, 3}
print('Só em b:', set_b - set_a)         # {7, 8, 9}


# 6) Agenda de contatos
agenda = {}
while True:
    nome = input('Nome do contato (vazio para sair): ')
    if nome == '':
        break
    telefone = input('Telefone: ')
    email = input('Email: ')
    agenda[nome] = {'telefone': telefone, 'email': email}

for nome, dados in agenda.items():
    print(f"{nome} -> tel: {dados['telefone']}, email: {dados['email']}")


# 7) Primeiro elemento duplicado
def achar_primeiro_duplicado(lista):
    vistos = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return -1

testes = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 2, 1],
    [7, 7, 1, 2, 3],
]
for teste in testes:
    print(achar_primeiro_duplicado(teste))
