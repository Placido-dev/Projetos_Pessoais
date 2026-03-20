# BÁSICO
print('Guilherme')

a = 3
b = 5
multiplicacao = (2 * a) * (3 * b)
print(f'A multiplicação deu: {multiplicacao}')

c = 5
d = 10
e = 15
soma = c + d + e
print(f'A soma deu: {soma}')

salario = 750
aumento = 15
resultado_final = salario + (salario * aumento / 100)
print(f'O aumento será de: {resultado_final}')

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite o segundo número: '))
soma_dos_numeros = primeiro_numero + segundo_numero
print(f'A soma dos números digitados é: {soma_dos_numeros}')

numero = float(input('Digite um valor em metros: '))
converter_em_milimetros = numero * 1000
print(f'O valor convertido para milimetros: {converter_em_milimetros}')

salario2 = int(input('Digite seu salario: '))
porcetagem_do_aumento = int(input('Digite a porcentagem do aumento: '))
novo_salario = salario2 + (salario2 * porcetagem_do_aumento / 100)
print(
    f'''
    A porcentagem do aumento será de {porcetagem_do_aumento} % 
    e o seu novo salario é de: {novo_salario}
    '''
)

preco_mercadoria = int(input('Digite o preço da mercadoria: '))
percentual_desconto = int(input('Digite o valor do desconto: '))
subtracao = preco_mercadoria - (preco_mercadoria * percentual_desconto / 100)
print(
    f'''
    O desconto é de: {percentual_desconto} %
    Valor total a pagar com desconto: {subtracao}
    '''
)

distancia = float(input('Digite a distância em km: '))
velocidade_media = float(input('Digite a velocidade média do carro: '))
tempo = distancia / velocidade_media
print(
    f'''
    A distância será de: {distancia} km
    A velocidade média será de: {velocidade_media} km/h
    Logo o tempo da viagem será de: {tempo:.2f} horas.
    '''
)

temperatura = int(input('Digite a temperatura: '))
conversao_F = (temperatura * 9 / 5) + 32
print(
    f'''
    A temperatura digitada foi: {temperatura} ºC
    Convertendo para farenheit: {conversao_F} ºF
    '''
)

km_percorrido_usuario = float(input('Digite a quantidade de km percorrido: '))
dias_alugado = int(input('Digite a quantidade de dias que o carro foi alugado: '))

diaria = 60
valor_por_km = 0.15

calculo_final = (dias_alugado * diaria) + (km_percorrido_usuario * valor_por_km)
print(
    f'''
    Você alugou o carro por {dias_alugado} dias, 
    Valor total a pagar: {calculo_final:.2f} R$.
    '''
)

qtd_cigarros_dia = int(input('Digite quantos cigarros você fuma por dia: '))
anos_fumando = float(input('Digite quantos anos você fuma: '))

numero_dias_fumando = anos_fumando * 365
total_cigarros_fumados_no_periodo = qtd_cigarros_dia * numero_dias_fumando
minutos_perdidos = total_cigarros_fumados_no_periodo * 10
dias_perdidos = minutos_perdidos / 1440

print(
    f'''
    Você fuma {qtd_cigarros_dia} cigarros no dia, durante {anos_fumando} anos.
    Se continuar assim vai pro saco preto, você já perdeu {dias_perdidos:.2f} dias de vida.
    '''
)

velocidade = int(input('Digite a velocidade: '))
limite = 80
excesso = velocidade - limite
multa = excesso * 5

if velocidade >= limite:
    print(
        f'''
        Você foi multado, sua velocidade foi de {velocidade},
        E terá que pagar uma multa de {multa:.2f} R$.
        '''
    )
else:
    print('Passou sem multa')


numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if numero_1 > numero_2:
    print(
        f'''
        Printando o primeiro valor: {numero_1}
    ''')
else:
    print(
        f'''
        Printando o segundo valor: {numero_2}
    ''')

seu_salario = float(input('Digite o seu salário: '))
aumento = 0

if seu_salario > 1250:
    aumento = seu_salario * 0.10
    novo_salario = seu_salario + aumento
    print(
        f'''
        Seu salário terá um aumento de: R${aumento:.2f} reais.
        Você receberá R${novo_salario:.2f} reais.
        ''')
else:
    aumento = seu_salario * 0.15
    novo_salario = seu_salario + aumento
    print(
        f'''
        Seu salário terá um aumento de: R${aumento:.2f} reais.
        Você receberá R${novo_salario:.2f} reais.
        ''')

distancia_desejada = float(input('Digite a distancia que quer andar em km: '))
tarifa_1 = 0.50
tarifa_2 = 0.45

if distancia_desejada <= 200:
    total = tarifa_1 * distancia_desejada
else:
    total = tarifa_2 * distancia_desejada

print(
    f'''
    Total a pagar da tarifa: R${total} reais.
    ''')

minutos = int(input('Digite os minutos que utilizou: '))

if minutos < 200:
    preco = 0.20
elif minutos > 400:
    preco = 0.18
else:
    preco = 0.15

print(f'Você vai pagar este mês: R${minutos * preco:.2f}')

first_number = float(input('Digite um número: '))
second_number = float(input('Digite outro número: '))

adicao = first_number + second_number
subtracao = first_number - second_number
multiplicacao = first_number * second_number
divisao = first_number / second_number

choice = input('Digite qual dessas operações você quer fazer (+, -, *, /): ')

if choice == '+':
    print(f'Você escolheu {choice}, então iremos somar os números {first_number} e {second_number} total = {adicao}')
elif choice == '-':
    print(f'Você escolheu {choice}, então iremos subtrair os números {first_number} e {second_number} total = {subtracao}')
elif choice == '*':
    print(f'Você escolheu {choice}, então iremos multiplicar os números {first_number} e {second_number} total = {multiplicacao}')
elif choice == '/':
    print(f'Você escolheu {choice}, então iremos dividir os números {first_number} e {second_number} total = {divisao}')
else:
    print('Preciso que digite uma operação dentre as que pedi.')

valor_casa = float(input('Digite o valor da casa para a compra: '))
salario_atual = float(input('Digite o seu salário atual: '))
anos_a_pagar = int(input('Digite a quantidade de anos que vai pagar: '))

meses_a_pagar = anos_a_pagar * 12

porcentagem_necessaria = salario_atual * 0.30

prestacao_mensal = valor_casa / meses_a_pagar

if porcentagem_necessaria <= prestacao_mensal:
    print('Não poderá comprar a casa, a prestação mensal não pode ser superior a 30% do seu salário ')
else:
    print(
    f'''
    Aprovado, sua prestação mensal ficou em R${prestacao_mensal:.2f} reais mensais 
    ''')

tipo_instalacao = str(input('Digite o tipo de instalação feita (para residencias digite R, para industrias digite I e digite C para comercios): '))
qtd_consumido = float(input('Digite a quantidade de kWh consumidas: '))

if tipo_instalacao == 'R' or tipo_instalacao == 'r':
    if qtd_consumido <= 500:
        tarifa = 0.40
    else:
        tarifa = 0.65
elif tipo_instalacao == 'I' or tipo_instalacao == 'i':
    if qtd_consumido <= 1000:
        tarifa = 0.55
    else:
        tarifa = 0.60
elif tipo_instalacao == 'C' or tipo_instalacao == 'c':
    if qtd_consumido <= 5000:
        tarifa = 0.55
    else:
        tarifa = 0.60
else:
    print('Digite R/I/C para calcularmos.')

preco_total = qtd_consumido * tarifa    

print(
    f'''
    Você digitou a opção {tipo_instalacao},
    Sua quantidade consumida foi de {qtd_consumido} kWh,
    Sua conta será no valor de R${preco_total:.2f} reais.
    ''')

# invertendo condições

a = int(input('Digite um número: '))

if a < 10:
    print(f"{a} é menor que 10")
elif a >= 10 and a < 20:
    print(f'{a} é maior que 10 e menor que 20')
else:
    print(f'{a} é maior que 20')

# if else elif

hora = int(input('Digite um número: '))

if hora < 12:
    print(f"Bom dia!")
elif hora >= 12 and hora <= 18:
    print(f'Boa tarde!')
else:
    print(f'Boa noite!')

# if else elif

media = int(input('Digite sua média: '))

if media < 4:
    print('Reprovado!')
elif media < 7:
    print('Recuperação!')
else:
    print('Passou!')


# while

x = 1

while x <= 3:
    print(f'X vale: {x}')
    x = x + 1
    print(f'X agora virou: {x}, somamos mais 1')
    if x == 4:
        print('Chegou no 4, acabou o loop!')
    else:
        print('Continuaremos a adicionar + 1 até chegar em 4!')

# while

x = 10

while x != 0:
    print(f'Contagem regressiva: {x}!')
    x = x - 1
    if x == 0:
        print('Fogo!')

# while

fim = int(input('Digite o último número do loop: '))
print(f'Irei imprimir até o {fim}, go!')
# contador
x = 1

# bloco
while x <= fim:
    print(x)
    x = x + 1
    if x == fim:
        print(f'Chegamos ao número: {x}, encerrando contagem')
        break

fim = int(input('Digite o último número do loop: '))
print(f'Irei imprimir os valores ímpares do {fim}, go!')
# contador
x = 0

# bloco
while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1

n = int(input('Tabuada do: '))
x = 1

while x <= 10:
    print(f'{n} x {x} = {n * x}')
    x = x + 1

inicio = int(input('Tabuada do: '))
fim = int(input('Digite o valor para parar: '))

x = 0

while x <= fim:
    print(f'{inicio} x {x} = {inicio * x}')
    x = x + 1

primeiro_n = int(input('Digite o valor: '))
repeticao = int(input('Digite o valor para repetir: '))
result = 0

contador = repeticao

while contador > 0: 
    result = result + primeiro_n
    print(f'{primeiro_n} x {repeticao} = {result}')
    contador = contador - 1

primeiro_n = int(input('Digite um número para dividir: ')) # é o número que vai diminuindo
repeticao = int(input('Digite a quantidade de vezes para dividir: ')) # é o número que vai subtrair

contador = 0 # é quantas vezes conseguiu subtrair
resto = 0

while primeiro_n >= repeticao:
    primeiro_n = primeiro_n - repeticao
    print(primeiro_n)
    contador = contador + 1

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f'Resposta da questão {questao}: ')
    if questao == 1 and resposta == 'b' or resposta == 'B':
        pontos = pontos + 1
    elif questao == 2 and resposta == 'a' or resposta == 'A':
        pontos = pontos + 1
    elif questao == 3 and resposta == 'c' or resposta == 'C':
        pontos = pontos + 1
    questao = questao + 1
print(f'O aluno fez {pontos} ponto(s)')

x = 1
soma = 0

while x <= 5:
    n = int(input(f'{x} Digite um número: '))
    soma = soma + n
    x = x + 1
print(f'Média: {soma / 5:5.2f}')

deposito = int(input('Digite o seu deposito: '))
taxa_juros = int(input('Digite a taxa de juros: ')) / 100

mes = 1
valor_total = deposito

while mes <= 24:
    taxa_juros_mes = taxa_juros * valor_total
    valor_total = valor_total + taxa_juros
    rendimento = valor_total - deposito
    print('-' * 40)
    print(f'Mês: {mes}')
    print(f'Valor total: R$ {valor_total:.2f}')
    print(f'Juros do mês: R$ {taxa_juros_mes:.2f}')
    print(f'Rendimento acumulado: R$ {rendimento:.2f}')
    print('-' * 40)
    mes = mes + 1

n = 0
qtd_num = 0

while True:
    p = int(input('Digite um número para somar ou digite 0 para sair do laço: '))
    if p == 0:
        break
    qtd_num += 1
    n += p
    m = n / qtd_num
print(f'Quantidade de números digitados: {qtd_num}')
print(f'Soma dos números digitados: {n}')
print(f'Média dos números digitados: {m:.2f}')


# CAIXA REGISTRADORA

cod_1 = 1
cod_2 = 2
cod_3 = 3
cod_5 = 5
cod_9 = 9

preco_1 = 0.50
preco_2 = 1.00
preco_3 = 4.00
preco_5 = 7.00
preco_9 = 8.00

produto_escolhido = 0
qtd_comprada = 0
sub_total = 0
total_geral = 0

print('=' * 50)
print('CAIXA REGISTRADORA DO JARDEL BOLIVIANO')
print('=' * 50)
print('Produtos disponíveis:')
print('[1] Produto 1  -> R$ 0.50')
print('[2] Produto 2  -> R$ 1.00')
print('[3] Produto 3  -> R$ 4.00')
print('[5] Produto 5  -> R$ 7.00')
print('[9] Produto 9  -> R$ 8.00')
print('=' * 50)
print('Digite [0] no código do produto para finalizar a compra.')
print('=' * 50)

while True:

    print('\n' + '-' * 50)
    produto_escolhido = int(input('Digite o código do produto: '))

    if produto_escolhido == 0:
        print('-' * 50)
        print('Encerrando compra...')
        print('Calculando valor total da compra...')
        print('-' * 50)
        print(f'TOTAL A PAGAR: R$ {total_geral:.2f}')
        print('=' * 50)
        print('Obrigado por comprar no Jardel!')
        print('=' * 50)
        break

    qtd_comprada = int(input('Digite a quantidade comprada: '))

    if produto_escolhido == cod_1:
        sub_total = preco_1 * qtd_comprada
    elif produto_escolhido == cod_2:
        sub_total = preco_2 * qtd_comprada
    elif produto_escolhido == cod_3:
        sub_total = preco_3 * qtd_comprada
    elif produto_escolhido == cod_5:
        sub_total = preco_5 * qtd_comprada
    elif produto_escolhido == cod_9:
        sub_total = preco_9 * qtd_comprada

    if produto_escolhido == cod_1:
        total_geral += sub_total
        print('-' * 50)
        print('Produto adicionado com sucesso!')
        print(f'Código do produto: {produto_escolhido}')
        print(f'Quantidade comprada: {qtd_comprada}')
        print(f'Subtotal do produto: R$ {sub_total:.2f}')
        print(f'Total acumulado: R$ {total_geral:.2f}')
        print('-' * 50)
    elif produto_escolhido == cod_2:
        total_geral += sub_total
        print('-' * 50)
        print('Produto adicionado com sucesso!')
        print(f'Código do produto: {produto_escolhido}')
        print(f'Quantidade comprada: {qtd_comprada}')
        print(f'Subtotal do produto: R$ {sub_total:.2f}')
        print(f'Total acumulado: R$ {total_geral:.2f}')
        print('-' * 50)        
    elif produto_escolhido == cod_3:
        total_geral += sub_total
        print('-' * 50)
        print('Produto adicionado com sucesso!')
        print(f'Código do produto: {produto_escolhido}')
        print(f'Quantidade comprada: {qtd_comprada}')
        print(f'Subtotal do produto: R$ {sub_total:.2f}')
        print(f'Total acumulado: R$ {total_geral:.2f}')
        print('-' * 50)        
    elif produto_escolhido == cod_5:
        total_geral += sub_total
        print('-' * 50)
        print('Produto adicionado com sucesso!')
        print(f'Código do produto: {produto_escolhido}')
        print(f'Quantidade comprada: {qtd_comprada}')
        print(f'Subtotal do produto: R$ {sub_total:.2f}')
        print(f'Total acumulado: R$ {total_geral:.2f}')
        print('-' * 50)        
    elif produto_escolhido == cod_9:
        total_geral += sub_total
        print('-' * 50)
        print('Produto adicionado com sucesso!')
        print(f'Código do produto: {produto_escolhido}')
        print(f'Quantidade comprada: {qtd_comprada}')
        print(f'Subtotal do produto: R$ {sub_total:.2f}')
        print(f'Total acumulado: R$ {total_geral:.2f}')
        print('-' * 50)        
    else:
        print('Código digitado inválido.')

valor = int(input('Digite o valor à pagar: '))
cedulas = 0
atual = 100
a_pagar = valor

while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f'Cédulas {cedulas} de R${atual}')
        if a_pagar == 0:
            break

        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1

        cedulas = 0

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