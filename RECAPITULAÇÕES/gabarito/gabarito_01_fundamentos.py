# GABARITO 01 - FUNDAMENTOS
# Tente resolver sozinho antes de olhar aqui!

# 1) Classificador de idade
idade = int(input('Digite sua idade: '))
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')

# 2) Par ou ímpar, positivo ou negativo
numero = int(input('Digite um número: '))
par_impar = 'par' if numero % 2 == 0 else 'ímpar'
if numero > 0:
    sinal = 'positivo'
elif numero < 0:
    sinal = 'negativo'
else:
    sinal = 'zero'
print(f'O número é {par_impar} e {sinal}.')

# 3) Maior de três
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c
print(f'O maior é: {maior}')

# 4) Tabuada com while
n = int(input('Tabuada de qual número? '))
x = 1
while x <= 10:
    print(f'{n} x {x} = {n * x}')
    x += 1

# 5) Soma até digitar 0
soma = 0
qtd = 0
while True:
    valor = int(input('Digite um número (0 para sair): '))
    if valor == 0:
        break
    soma += valor
    qtd += 1
print(f'Quantidade: {qtd}')
print(f'Soma: {soma}')
if qtd > 0:
    print(f'Média: {soma / qtd:.2f}')
else:
    print('Nenhum número digitado, sem média.')

# 6) Adivinhação simples
secreto = 42
tentativas = 0
while True:
    palpite = int(input('Tente adivinhar o número: '))
    tentativas += 1
    if palpite < secreto:
        print('Maior!')
    elif palpite > secreto:
        print('Menor!')
    else:
        print('Acertou!')
        break
print(f'Você usou {tentativas} tentativa(s).')

# 7) FizzBuzz
x = 1
while x <= 30:
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
    x += 1
