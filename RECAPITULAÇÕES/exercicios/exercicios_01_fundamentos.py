# EXERCÍCIOS 01 - FUNDAMENTOS (variáveis, if/elif/else, while)
# Resolva aqui mesmo. Depois compare com gabarito/gabarito_01_fundamentos.py
#
# Dica: rode o arquivo aos poucos (comente o que ainda não fez) para testar
# só o exercício que você está resolvendo.

# -----------------------------------------------------------------------
# 1) Classificador de idade
# Peça a idade do usuário e imprima:
#   "Criança" se < 12
#   "Adolescente" se >= 12 e < 18
#   "Adulto" se >= 18 e < 60
#   "Idoso" se >= 60

'''
idade = int(input('Digite sua idade: '))
if idade < 12:
    print(f'Sua idade é {idade}, então vc é Criança.')
elif idade >= 12 and idade < 18:
    print(f'Sua idade é {idade}, então vc é Adolescente.')
elif idade >= 18 and idade < 60:
    print(f'Sua idade é {idade}, então vc é Adulto.')    
elif idade > 60:
    print(f'Sua idade é {idade}, então vc é Idoso.')
'''

# -----------------------------------------------------------------------
# 2) Par ou ímpar, positivo ou negativo
# Peça um número inteiro e diga se ele é par/ímpar E positivo/negativo/zero
# em uma única frase. Ex: "O número é par e positivo."

'''
numero = int(input('Digite um número: '))

if numero % 2 == 0 and numero > 0:
    print('par e positivo')
elif numero % 2 != 0 and numero < 0:
    print('ímpar e negativo')
else:
    print('é zero')
'''

# -----------------------------------------------------------------------
# 3) Maior de três (sem usar max())
# Peça três números e imprima o maior deles, usando apenas if/elif/else.
# (Você já fez algo parecido no main.py com uma função - tente refazer
# sem olhar lá.)
'''
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

if primeiro >= segundo and primeiro >= terceiro:
    print(primeiro)
elif segundo >= primeiro and segundo >= terceiro:
    print(segundo)
else:
    print(terceiro)
'''
# -----------------------------------------------------------------------
# 4) Tabuada com while
# Peça um número e imprima a tabuada dele de 1 a 10 usando while
# (não use for).

'''
try:
    numero = int(input('Digite um número inteiro para ver a tabuada dele de 1 a 10: '))
    if numero < 0:
        print('Número menor do que 0 não funciona.')
        quit()
    contador = 0
    while contador < 10:
        contador += 1
        multiplicar = numero * contador
        print(f'{numero} * {contador} = {multiplicar}')
except ValueError:
    print('Digite só números.')
'''

# -----------------------------------------------------------------------
# 5) Soma até digitar 0
# Use um while True: peça números ao usuário e vá somando.
# Quando o usuário digitar 0, pare o loop e imprima:
#   - quantos números foram digitados
#   - a soma total
#   - a média (cuidado com divisão por zero se o primeiro digitado já for 0)
'''
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
 '''
# -----------------------------------------------------------------------
# 6) Adivinhação simples
# Defina um número secreto fixo (ex: 42). Em um while True, peça um
# palpite ao usuário. Diga "Maior!" se o palpite for menor que o secreto,
# "Menor!" se for maior, e "Acertou!" quando for igual, encerrando o loop.
# Ao final, imprima quantas tentativas o usuário usou.



# -----------------------------------------------------------------------
# 7) FizzBuzz (clássico, mas revisa muito bem if/while)
# Usando while, percorra de 1 até 30. Para múltiplos de 3 imprima "Fizz",
# para múltiplos de 5 imprima "Buzz", para múltiplos de ambos imprima
# "FizzBuzz", senão imprima o próprio número.
