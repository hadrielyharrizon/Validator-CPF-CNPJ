'''
CPF and CNPJ Validator

This script allows you to validate CPF and CNPJ numbers
based on the official rules for verifying digits.

Author: Hadriely Harrizon
'''
import sqlite3


def clean_doc(doc):
    return ''.join(filter(str.isdigit, doc))

def formatcpf(cpf):
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

def formatcnpj(cnpj):
    return f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"


conn = sqlite3.connect('documentos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        numero TEXT
    )
''')
conn.commit()



while True:

    print ("Validação de CPF/CNPJ");
    doc_type = input ("CPF - 1 | CNPJ - 2: | Ver todos - 3: ");

    if doc_type == "1":
        doc = input("Digite o CPF: ")
        documento_limpo = clean_doc(doc)
        formattedcpf = input("Deseja seu CPF formatado? (s/n) ").strip().lower()

        if formattedcpf == "s":
            print('CPF formatado: ', formatcpf(documento_limpo))
        elif formattedcpf == "n":
            print('CPF limpo:', documento_limpo)
        else:
            print('Opção inválida.')

        cursor.execute("INSERT INTO documentos (tipo, numero) VALUES (?, ?)", ("CPF", documento_limpo))
        conn.commit()
        cursor.execute("SELECT * FROM documentos WHERE numero = ?", (documento_limpo,))
        if cursor.fetchone():
            print("Este documento já está armazenado.")
        else:
            cursor.execute("INSERT INTO documentos (tipo, numero) VALUES (?, ?)", ("CPF", documento_limpo))  # ou "CNPJ"
            conn.commit()
            print("Documento salvo com sucesso.")


    elif doc_type == "2":
        doc = input("Digite o CNPJ: ")
        documento_limpo = clean_doc(doc)
        formattedcnpj = input('Deseja seu CNPJ formatado? (s/n)').strip().lower()

        if formattedcnpj == "s":
            print('CNPJ formatado:', formatcnpj(documento_limpo))
        elif formattedcnpj == 'n':
            print("CNPJ limpo:", documento_limpo)
        else:
            print('Opção inválida.')
        cursor.execute("INSERT INTO documentos (tipo, numero) VALUES (?, ?)", ("CNPJ", documento_limpo))
        conn.commit()

        cursor.execute("SELECT * FROM documentos WHERE numero = ?", (documento_limpo,))
        if cursor.fetchone():
            print("Este documento já está armazenado.")
        else:
            cursor.execute("INSERT INTO documentos (tipo, numero) VALUES (?, ?)", ("CPF", documento_limpo))  # ou "CNPJ"
            conn.commit()
            print("Documento salvo com sucesso.")

    elif doc_type == "3":
        cursor.execute("SELECT tipo, numero FROM documentos")
        registros = cursor.fetchall()
        if registros:
            print("\n--- Documentos Armazenados ---")
            for tipo, numero in registros:
                print(f"{tipo}: {numero}")
        else:
            print("Nenhum documento armazenado.")

    else:
        print('Opção inválida.')

    continuar = input("Deseja validar outro documento? (s/n) ")
    if continuar == "n":
        print("Encerrando...")
        break

conn.close()


