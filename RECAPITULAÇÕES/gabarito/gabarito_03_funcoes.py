# GABARITO 03 - FUNÇÕES
# Tente resolver sozinho antes de olhar aqui!

# 1) eh_primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

for n in [0, 1, 2, 7, 10, 17, 21]:
    print(n, eh_primo(n))


# 2) calcular_total com valor padrão
def calcular_total(preco, quantidade, desconto=0):
    total = preco * quantidade
    return total - (total * desconto / 100)

print(calcular_total(100, 2))              # 200
print(calcular_total(100, 2, desconto=10))  # 180.0


# 3) estatisticas - retorno múltiplo
def estatisticas(lista):
    return min(lista), max(lista), sum(lista) / len(lista)

menor, maior, media = estatisticas([4, 8, 1, 9, 3])
print(f'Menor: {menor} | Maior: {maior} | Média: {media:.2f}')


# 4) fatorial recursivo
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(0))  # 1
print(fatorial(5))  # 120


# 5) fibonacci recursivo
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=' ')  # 0 1 1 2 3 5 8 13
print()


# 6) função como parâmetro
def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

print(aplicar_operacao(3, 4, soma))        # 7
print(aplicar_operacao(3, 4, multiplica))  # 12


# 7) validador de senha
def senha_valida(senha):
    if len(senha) < 8:
        return False
    tem_maiuscula = False
    tem_numero = False
    for c in senha:
        if c.isupper():
            tem_maiuscula = True
        if c.isdigit():
            tem_numero = True
    return tem_maiuscula and tem_numero

for s in ['abc123', 'Abcdefgh1', 'abcdefgh1', 'ABCDEFGH']:
    print(s, senha_valida(s))
