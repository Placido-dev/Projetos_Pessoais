import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()
connection = None

connection = pymysql.connect(
    host='localhost',
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    cursorclass=pymysql.cursors.DictCursor
)

adicionar_series = input('Digite a série para cadastrar no banco: ').strip()
status_validos = {'plan_to_watch', 'watching', 'paused', 'completed', 'dropped'}

while True:
    adicionar_status = input('Digite o status da série (plan_to_watch, watching, paused, completed, dropped): ').strip().lower()
    if adicionar_status in status_validos:
        break
    print(f"Status inválido: '{adicionar_status}'. Use um destes: {', '.join(sorted(status_validos))}")

while True:
    adicionar_nota = input('Dê uma nota para a série (0 a 10) ou deixe vazio: ').strip()
    if adicionar_nota == '':
        adicionar_nota = None
        break
    if adicionar_nota.isdigit():
        adicionar_nota = int(adicionar_nota)
        if 0 <= adicionar_nota <= 10:
            break
    print("[ERRO] Digite um número entre 0 e 10, ou deixe vazio.")

adicionar_comentario = input('Adicione uma nota ou observação, caso queira: ').strip()
if adicionar_comentario == '':
    adicionar_comentario = None

while True:
    adicionar_estrela = input('Digite 1 para favoritar, ou 0 para não: ').strip()
    if adicionar_estrela in ('0', '1'):
        adicionar_estrela = int(adicionar_estrela)
        break
    print("[ERRO] Digite apenas 0 ou 1.")

def sql_create_database():
    sql_create_db = '''
    CREATE DATABASE IF NOT EXISTS series;
    '''
    return sql_create_db

def use_database():
    sql_use_db = 'USE series;'
    return sql_use_db

def create_table_favoritos():
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS series_favoritas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        status ENUM('plan_to_watch','watching','paused','completed','dropped') NOT NULL DEFAULT 'plan_to_watch',

        rating TINYINT NULL,
        notes TEXT NULL,
        is_favorite BOOLEAN NOT NULL DEFAULT 0,

        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        deleted_at DATETIME NULL,

        UNIQUE KEY uq_series_favoritas_name_active (name, deleted_at),
        INDEX idx_series_favoritas_deleted_at (deleted_at),
        INDEX idx_series_favoritas_status (status),
        INDEX idx_series_favoritas_is_favorite (is_favorite),
        INDEX idx_series_favoritas_rating (rating)
    );
    '''
    return sql_create_table

def inserts():
    sql_inserts = '''
    INSERT INTO series.series_favoritas (name, status, created_at, updated_at, deleted_at, rating, notes, is_favorite)
    VALUES (%s, %s, NOW(), NOW(), NULL, %s, %s, %s);
    '''
    return sql_inserts

def read_rows():
    sql_read = '''
    SELECT * FROM series.series_favoritas WHERE deleted_at IS NULL 
    ORDER BY created_at DESC 
    LIMIT 1;    
    '''
    return sql_read

def update_rows():
    sql_update = '''
    UPDATE series.series_favoritas 
    SET status = %s
    WHERE id = %s
    AND deleted_at IS NULL;
    '''
    return sql_update

def hard_delete_rows():
    sql_delete = '''
    DELETE FROM series.series_favoritas 
    WHERE id = %s;
    '''
    return sql_delete

def soft_delete():
    sql_soft_delete = '''
    UPDATE series.series_favoritas 
    SET deleted_at = NOW()
    WHERE id = %s;
    '''
    return sql_soft_delete

try:
    with connection.cursor() as cursor:
        
        # CREATE_DB (IF NOT EXISTS)
        print('[DEBUG] Criando/selecionando DB e tabela...')
        cursor.execute(sql_create_database())
        # USE DB
        cursor.execute(use_database())
        # CREATE TABLE (IF NOT EXISTS)
        cursor.execute(create_table_favoritos())
        # INSERT INTO
        print(f'[DEBUG] Inserindo: name={adicionar_series!r}, status={adicionar_status!r}')
        cursor.execute(inserts(), (adicionar_series, adicionar_status, adicionar_nota, adicionar_comentario, adicionar_estrela))
        print(f'[DEBUG] Linhas inseridas: {cursor.rowcount} | lastrowid: {cursor.lastrowid}')
        # SAVE ROWS
        connection.commit()
        print('[DEBUG] Commit OK')
        # READ_ROWS
        cursor.execute(read_rows())
        result = cursor.fetchall()
        print(f'[DEBUG] Total de registros retornados: {len(result)}')
        # ITERATION FOR DEBUG
        for i, linha in enumerate(result, start=1):
            print(f'''
        [DEBUG] Registro {i}
        id: {linha['id']}
        name: {linha['name']}
        status: {linha['status']}
        rating: {linha['rating']}
        ''')
            
except pymysql.MySQLError as e:
    print('Erro no banco:', e)

finally:
    if connection and connection.open:
        connection.close()
        print('Conexão fechada.')