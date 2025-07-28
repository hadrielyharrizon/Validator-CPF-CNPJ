import sqlite3

def create_table():
# Cria ou conecta ao banco
    conn = sqlite3.connect('documentos.db')
    cursor = conn.cursor()

    # Cria a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            numero TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    conn.close()

    print("Banco de dados inicializado com sucesso.")
    
create_table()
