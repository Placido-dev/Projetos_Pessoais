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