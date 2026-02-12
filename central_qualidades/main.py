import pandas as pd


data = pd.read_csv(r'C:\Users\Pichau\Downloads\projetos\Projetos_Pessoais\central_qualidades\data_raw\clientes.csv')

colunas_linhas = data.shape
print('Contagem de linhas e colunas')
print(colunas_linhas)

rows_empty = data.isna().sum()
print('Contagem das colunas com vazios')
print(rows_empty)

filtro = data.fillna('falta_dados_aqui')


lista_columns = [
    'nome',
    'email',
    'cidade',
    'status',
]

filtro[lista_columns] = filtro[lista_columns].astype(str).apply(lambda s: s.str.strip())
print(filtro)

