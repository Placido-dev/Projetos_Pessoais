import pandas as pd
import pymysql
from dotenv import load_dotenv
import os

df = pd.read_csv(r'C:\Users\Pichau\Downloads\CRUD\teste_csv - import.csv')

def padronizar_colunas(df):
    df = df.rename(columns={
        'Nome': 'first_name',
        'Sobrenome': 'last_name',
        'Email': 'email'
    })
    return(df)

def limpar_strings(df):
    df['email'] = df['email'].astype(str).str.strip().str.lower() 
    df["first_name"] = df["first_name"].astype(str).str.strip() 
    df["last_name"] = df["last_name"].astype(str).str.strip()
    return(df)

def reportar_metricas(df):
    total_registros_csv = len(df)
    vazios = (df['email'] == '').sum()
    df_sem_vazio = df[df['email'] != '']
    qtd_duplicado = df_sem_vazio['email'].duplicated().sum()

    print('CSV contém', total_registros_csv, 'registros')
    print('Emails em branco: ', vazios)
    print('Emails limpos: ', len(df_sem_vazio))

    if qtd_duplicado == 0:
        print('CSV limpo, sem duplicados')
    else:
        print(f'Temos {qtd_duplicado} duplicado(s)')
    return(df) 

def tratar_dados(df):
    df_limpo = df[df['email'] != '']
    df_final = df_limpo.drop_duplicates(subset=['email'], keep='last')

    return df_final

data_filtrada = (df.pipe(padronizar_colunas).pipe(limpar_strings).pipe(reportar_metricas).pipe(tratar_dados))
print(data_filtrada.head())
print("Total final:", len(data_filtrada))

data_em_dic = data_filtrada.to_dict(orient='records')

if len(data_em_dic) != len(data_filtrada):
    print('Algo errado')
else:
    print(len(data_em_dic))

# Conectar DB

load_dotenv()

user_db = os.getenv('user')
password_db = os.getenv('password')
name_db = os.getenv('database')

connection = pymysql.connect(
        host='localhost',
        user=user_db,
        password=password_db,
        database=name_db,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_selects(connection, query1):
    print('Executando a query', query1)
    with connection.cursor() as cursor:
        cursor.execute(query1)
        return cursor.fetchone()
    
def execute_inserts(connection, query2):
    print('Executando a query:', query2)
    with connection.cursor() as cursor:
        cursor.executemany(query2, data_em_dic)
        afetadas = cursor.rowcount
    connection.commit()
    print("Linhas afetadas:", afetadas)
    
try:

    query1 = 'SELECT COUNT(*) AS total FROM users;'
    result = execute_selects(connection, query1)
    print(f'Temos: {result} registros no banco')

    query2 = """INSERT INTO data_quality_hub.users (id, email, first_name, last_name, created_at, deleted_at) 
    VALUES (UUID(), %(email)s, %(first_name)s, %(last_name)s, NOW(), NULL)
    ON DUPLICATE KEY UPDATE first_name = VALUES(first_name), last_name  = VALUES(last_name);"""
    insert = execute_inserts(connection, query2)
    print('Querys realizadas!')

    query3 = 'SELECT COUNT(*) AS total FROM users;'
    result3 = execute_selects(connection, query3)
    print(f'Após atualizar, temos: {result3} registros no banco')

except pymysql.Error as e:
    print('Erro em realizar as querys', e)
    connection.rollback()

finally:
    connection.close()
    print('Conexão encerrada')