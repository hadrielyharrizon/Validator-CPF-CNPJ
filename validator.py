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

def validar_cpf(cpf):
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i+1) - j) for j in range(i))
        dig = (soma * 10) % 11
        if dig == 10:
            dig = 0
        if dig != int(cpf[i]):
            return False
    return True

def validar_cnpj(cnpj):
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    dig1 = 11 - soma1 % 11
    if dig1 >= 10:
        dig1 = 0
    if dig1 != int(cnpj[12]):
        return False

    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    dig2 = 11 - soma2 % 11
    if dig2 >= 10:
        dig2 = 0
    return dig2 == int(cnpj[13])


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


