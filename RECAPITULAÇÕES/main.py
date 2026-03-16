# while

while True:
    valor_1 = int(input('Digite um número: ')) 
    valor_2 = int(input('Digite um outro número: ')) 

    soma = valor_1 + valor_2

    checagem = str(input(('Novo calculo [S/N]? ')))

    if checagem == 'S' or checagem == 's':
        print('Vamos calcular outros números.')    

    elif checagem == 'N' or checagem == 'n':
        print(f'Fim dos cálculos, soma dos números digitados = {soma}')
        break

    print(f'Soma dos números digitados = {soma}')