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