from flask import Flask, request, render_template
from validator import clean_doc, validar_cpf, validar_cnpj, formatcpf, formatcnpj
from init_db import create_table
import sqlite3

create_table
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/validate', methods=['POST'])
def validate():
    tipo = request.form['tipo']
    numero = clean_doc(request.form['numero'])  # limpa pontuação

    print(f'Recebido - Tipo: {tipo}, Número limpo: {numero}')

    conn = sqlite3.connect('documentos.db')
    cursor = conn.cursor()

    # Validação do número
    if tipo == 'CPF':
        valido = validar_cpf(numero)
        numero_formatado = formatcpf(numero)
    else:
        valido = validar_cnpj(numero)
        numero_formatado = formatcnpj(numero)

    if not valido:
        mensagem = f'{tipo} inválido!'
    else:
    # Verificação de duplicata no banco (número limpo)
        cursor.execute("SELECT * FROM documentos WHERE numero = ?", (numero,))
        if cursor.fetchone():
            mensagem = f"{tipo} já está armazenado: {numero_formatado}"
        else:
            cursor.execute("INSERT INTO documentos (tipo, numero) VALUES (?, ?)", (tipo, numero))
            conn.commit()
            mensagem = f"{tipo} salvo com sucesso: {numero_formatado}"

    conn.close()
    return render_template('result.html', mensagem=mensagem)

@app.route('/list')
def list_documents():
    conn = sqlite3.connect('documentos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tipo, numero FROM documentos")
    registros = cursor.fetchall()
    conn.close()
    return render_template('list.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)
