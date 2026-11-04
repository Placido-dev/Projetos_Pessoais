# EXERCÍCIOS 03 - FUNÇÕES
# Resolva aqui mesmo. Depois compare com gabarito/gabarito_03_funcoes.py

# -----------------------------------------------------------------------
# 1) Função com retorno simples
# Crie uma função eh_primo(numero) que retorna True se o número for primo,
# False caso contrário. Teste com vários números (0, 1, 2, 7, 10, 17, 21).


# -----------------------------------------------------------------------
# 2) Função com múltiplos parâmetros e valor padrão
# Crie uma função calcular_total(preco, quantidade, desconto=0) que
# retorna o valor total já aplicando o desconto (em %).
# Ex: calcular_total(100, 2) -> 200
#     calcular_total(100, 2, desconto=10) -> 180


# -----------------------------------------------------------------------
# 3) Função que retorna múltiplos valores (igual ao calcular_imc que
# você já tinha feito, mas agora para números)
# Crie estatisticas(lista) que retorna uma tupla (menor, maior, media)
# da lista de números recebida.


# -----------------------------------------------------------------------
# 4) Função recursiva - fatorial
# Crie fatorial(n) usando recursão (a função chamando ela mesma),
# sem usar while/for.
# fatorial(0) = 1
# fatorial(5) = 120


# -----------------------------------------------------------------------
# 5) Função recursiva - Fibonacci
# Crie fibonacci(n) que retorna o n-ésimo termo da sequência de Fibonacci
# (0, 1, 1, 2, 3, 5, 8, 13, ...), usando recursão.


# -----------------------------------------------------------------------
# 6) Função que recebe outra função como parâmetro
# Crie aplicar_operacao(a, b, operacao) onde "operacao" é uma função
# (por exemplo, você passa uma função soma(a, b) ou multiplica(a, b)).
# A função aplicar_operacao deve apenas chamar operacao(a, b) e retornar
# o resultado.
# Dica: isso é o começo de entender funções como "cidadãs de primeira
# classe" em Python - prepara terreno para lambdas e map/filter depois.


# -----------------------------------------------------------------------
# 7) Validador de senha (função com várias condições)
# Crie senha_valida(senha) que retorna True se a senha:
#   - tiver pelo menos 8 caracteres
#   - tiver pelo menos uma letra maiúscula
#   - tiver pelo menos um número
# e False caso contrário. Teste com várias senhas.
