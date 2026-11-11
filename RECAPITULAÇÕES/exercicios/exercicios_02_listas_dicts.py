# EXERCÍCIOS 02 - LISTAS, TUPLAS, DICTS, CONJUNTOS
# Resolva aqui mesmo. Depois compare com gabarito/gabarito_02_listas_dicts.py

# -----------------------------------------------------------------------
# 1) Lista de notas (revisão direta do que você já tinha feito)
# Peça 5 notas ao usuário, guarde numa lista, depois imprima:
#   - a maior nota
#   - a menor nota
#   - a média
# Tente resolver sem usar max()/min() primeiro, depois refaça usando.


# -----------------------------------------------------------------------
# 2) Lista sem repetidos, mantendo ordem
# Dada a lista abaixo, crie uma nova lista sem elementos repetidos,
# mantendo a ordem da primeira aparição de cada número.
# (Repare: isso é parecido com o exercício de "lista_3" que você já tinha
# feito juntando lista_1 e lista_2, mas agora numa lista só.)
numeros = [4, 5, 4, 2, 7, 5, 9, 2, 1, 4]
# resultado esperado: [4, 5, 2, 7, 9, 1]


# -----------------------------------------------------------------------
# 3) Contagem de palavras (dict)
# Dada a frase abaixo, conte quantas vezes cada palavra aparece e guarde
# num dicionário. Ignore maiúsculas/minúsculas.
frase = "o rato roeu a roupa do rei de roma o rato"
# resultado esperado (chaves podem vir em qualquer ordem):
# {'o': 2, 'rato': 2, 'roeu': 1, 'a': 1, 'roupa': 1, 'do': 1, 'rei': 1,
#  'de': 1, 'roma': 1}


# -----------------------------------------------------------------------
# 4) Inverter um dicionário
# Dado o dicionário abaixo, crie outro onde as chaves viram valores e os
# valores viram chaves.
capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
}
# resultado esperado: {'Brasília': 'Brasil', 'Paris': 'França', 'Tóquio': 'Japão'}


# -----------------------------------------------------------------------
# 5) Interseção e diferença com sets
# Dadas as duas listas abaixo, use set() para descobrir:
#   - quais números aparecem nas duas listas
#   - quais aparecem só na lista_a
#   - quais aparecem só na lista_b
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]


# -----------------------------------------------------------------------
# 6) Agenda de contatos (dict de dicts)
# Crie um dicionário vazio "agenda". Em um while True, peça:
#   - nome do contato (se digitar vazio "", encerra o loop)
#   - telefone
#   - email
# Guarde cada contato como agenda[nome] = {"telefone": ..., "email": ...}
# Ao final, imprima todos os contatos formatados, um por linha.


# -----------------------------------------------------------------------
# 7) Primeiro elemento duplicado (parecido com o que você já fez)
# Crie uma função achar_primeiro_duplicado(lista) que retorna o primeiro
# valor que se repete (considerando a ordem da lista), ou -1 se não houver
# nenhum repetido. Teste com:
testes = [
    [1, 2, 3, 4, 5],         # -> -1
    [1, 2, 3, 2, 1],         # -> 2
    [7, 7, 1, 2, 3],         # -> 7
]
