from flask import Flask, request, render_template
from validator import clean_doc, validar_cpf, validar_cnpj, formatcpf, formatcnpj
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/validate', methods=['POST'])
def validate():
    tipo = request.form['tipo']
    numero = clean_doc(request.form['numero'])  # limpa pontuação

    conn = sqlite3.connect('documentos.db')
    cursor = conn.cursor()

    # Validação do número
    if tipo == 'CPF':
        if not validar_cpf(numero):
            return "CPF inválido!"
        numero_formatado = formatcpf(numero)
    else:
        if not validar_cnpj(numero):
            return "CNPJ inválido!"
        numero_formatado = formatcnpj(numero)

    # Verificação de duplicata no banco (número limpo)
    cursor.execute("SELECT * FROM documentos WHERE numero = ?", (numero,))
    if cursor.fetchone():
        mensagem = f"{tipo} já está armazenado: {numero_formatado}"
    else:
        cursor.execute("INSERT INTO documentos (tipo, numero) VALUES (?, ?)", (tipo, numero))
        conn.commit()
        mensagem = f"{tipo} salvo com sucesso: {numero_formatado}"

    conn.close()
    return mensagem

if __name__ == '__main__':
    app.run(debug=True)
