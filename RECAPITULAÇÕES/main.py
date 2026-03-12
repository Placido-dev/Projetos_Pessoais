# while

x = 1
soma = 0

while x <= 5:
    n = int(input(f'{x} Digite um número: '))
    soma = soma + n
    x = x + 1
print(f'Média: {soma / 5:5.2f}')    