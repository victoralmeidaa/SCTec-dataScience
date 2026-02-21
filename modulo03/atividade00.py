import psycopg2 
from psycopg2 import sql
from psycopg2 import errors

def conectar():
    return psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='db_mundotech',
        user='postgres',
        password='Userroot'
    )

conn = conectar()
conn.autocommit = True
db_name = 'db_mundotech'
cur = conn.cursor()
try:    # CREATE DATABASE
    create_db_query = sql.SQL(
        'CREATE DATABASE {}'
    ).format(sql.Identifier(db_name))

    cur.execute(create_db_query)
    print(f'Banco de dados {db_name} criado com sucesso.')

except errors.DuplicateDatabase:
    print(f'Banco de dados {db_name} já existe. ignorando...')

except Exception as e:
    print('Erro inesperado: ', e)

try:    # CREATE TABLE
    create_table_query = '''
    CREATE TABLE name_table(
        coluna01 VARCHAR(255),
        coluna02 VARCHAR(255)
    )
'''
    cur.execute(create_table_query)
    print('Tabela criada com sucesso.')
except errors.DuplicateTable:
    print('Tabela já existe, Ignorando...')

except Exception as e:
    print(f'Erro Inesperado: ', e)


def insert_registro(coluna01, coluna02):
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute(
            '''
            INSERT INTO name_table (coluna01, coluna02)
            VALUES (%s, %s)
            RETURNING *
            ''',
            (coluna01, coluna02)
        )

        registro = cur.fetchone()
        conn.commit()
        print('Inserido: ', registro)

    except Exception as e:

        print('Erro no INSERT: ', e)

    finally:
        cur.close()
        conn.close()

def update_registro(novo_valor1, novo_valor2, criterio):
    conn = conectar()
    cur = conn.cursor()
    
    try:
        cur.execute(
            '''
            UPDATE name_table
            SET coluna01 = %s,
                coluna02 = %s
            WHERE coluna02 = %s
            RETURNING *
            ''',
            (novo_valor1, novo_valor2, criterio)
        )

        registros = cur.fetchall()
        conn.commit()

        print("Atualizados:", registros)

    except Exception as e:
        conn.rollback()
        print("Erro no UPDATE:", e)

    finally:
        cur.close()
        conn.close()

def delete_registro(criterio):
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute(
            '''
            DELETE FROM name_table
            WHERE coluna02 = %s
            RETURNING *
            ''',
            (criterio,)
        )

        registros = cur.fetchall()
        conn.commit()

        print("Deletados:", registros)

    except Exception as e:
        conn.rollback()
        print("Erro no DELETE:", e)

    finally:
        cur.close()
        conn.close()

def select_todos():
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute('SELECT * FROM name_table')
        registros = cur.fetchall()

        print("Registros encontrados:")
        for registro in registros:
            print(registro)

    except Exception as e:
        print("Erro no SELECT:", e)

    finally:
        cur.close()
        conn.close()

def select_por_coluna02(valor):
    conn = conectar()
    cur = conn.cursor()

    try:
        cur.execute(
            '''
            SELECT * FROM name_table
            WHERE coluna02 = %s
            ''',
            (valor,)
        )

        registros = cur.fetchall()

        print("Resultado da busca:")
        for registro in registros:
            print(registro)

    except Exception as e:
        print("Erro no SELECT:", e)

    finally:
        cur.close()
        conn.close()



insert_registro('texto1', 'texto2')
select_todos()
select_por_coluna02('texto2')
update_registro('novo_texto1', 'novo_texto2', 'texto2')
delete_registro('novo_texto2')
