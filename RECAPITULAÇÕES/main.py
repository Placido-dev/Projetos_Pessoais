# Listas, dicts, tuplas, conjuntos

lista_1 = []
lista_2 = []

while True:
    entrada_1 = int(input('Digite um número para adicionar a lista [0 para sair]: '))
    if entrada_1 == 0:
        print(f'Comando {entrada_1} digitado, sua primeira lista ficou: {lista_1}, respectivamente sua segunda lista: {lista_2}')
        break     
    entrada_2 = int(input('Digite outro número para adicionar na segunda lista: ')) 
    lista_1.append(entrada_1)
    lista_2.append(entrada_2)
    print(
        f'''
        Valor adicionado na primeira lista: {lista_1[-1]}.
        Valor adicionado na segunda lista: {lista_2[-1]}
        '''
)