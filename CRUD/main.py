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
        name VARCHAR(255) NOT NULL UNIQUE,
        status ENUM('plan_to_watch','watching','paused','completed','dropped') NOT NULL DEFAULT 'plan_to_watch',
        last_watched_at DATETIME NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        deleted_at DATETIME NULL,

        UNIQUE KEY uq_series_favoritas_name_active (name, deleted_at),
        INDEX idx_series_favoritas_deleted_at (deleted_at),
        INDEX idx_series_favoritas_status (status)
    );    
    '''
    return sql_create_table

def inserts():
    sql_inserts = '''
    INSERT INTO series.series_favoritas (name, status, last_watched_at, created_at, updated_at, deleted_at)
    VALUES ('The Mentalist', 'watching', NOW(), NOW(), NOW(), NULL);
    '''
    return sql_inserts

def read_rows():
    sql_read = '''
    SELECT * FROM series.series_favoritas;    
    '''
    return sql_read

def update_rows():
    sql_update = '''
    UPDATE series.series_favoritas 
    SET status = %s
    WHERE id = %s;
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
        cursor.execute(sql_create_database())
        # USE DB
        cursor.execute(use_database())
        # CREATE TABLE (IF NOT EXISTS)
        cursor.execute(create_table_favoritos())
        # INSERT INTO
        cursor.execute(inserts())
        # SAVE ROWS
        connection.commit()
        # READ_ROWS
        cursor.execute(read_rows())
        result = cursor.fetchall()
        print(result)


except pymysql.MySQLError as e:
    print('Erro no banco:', e)

finally:
    if connection and connection.open:
        connection.close()
        print('Conexão fechada.')