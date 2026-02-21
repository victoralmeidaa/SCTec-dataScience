import psycopg2
from psycopg2 import sql
from psycopg2 import errors

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='postgres',
    user='postgres',
    password='Userroot'
)

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


# try:    # INSERT TABLE
#     valor1 = 'texto1'
#     valor2 = 'texto2'

#     cur.execute('''
#         INSERT INTO name_table (coluna01, coluna02) 
#         VALUES (%s, %s)''', 
#         (valor1, valor2))
    
#     print('Registro inserido com sucesso.')
# except errors.DuplicateColumn:
#     print('Coluna já existe, Ignorando...')

# except Exception as e:
#     print(f'Erro ao inserir', e)


# UPDATE DATABASE
# novo_valor1 = 'texto1_autalizado'
# novo_valor2 = 'texto2_atualizado'
# valor_criterio = 'texto2'

# cur.execute(
#     'UPDATE name_table ' 
#     'SET coluna01 = %s, ' 
#     'coluna02 = %s ' 
#     'WHERE coluna02 = %s',
#     (novo_valor1, novo_valor2, valor_criterio)
# )
# print("Linhas afetadas:", cur.rowcount)
# conn.commit()
cur.execute('SELECT * FROM name_table')
rows = cur.fetchall()

for row in rows:
    print(row)

# DELETE
# valor_criterio = 'texto2_atualizado'
# cur.execute('''
#     DELETE FROM name_table
#     WHERE coluna02 = %s
#  ''', (valor_criterio,)
#  )
# conn.commit()

# SELECT table
cur.execute('SELECT * FROM name_table')
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()