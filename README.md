Validador de CPF e CNPJ
Este projeto é uma aplicação web simples desenvolvida em Python com Flask para validar CPF e CNPJ utilizando as regras oficiais de verificação dos dígitos verificadores. Além disso, armazena os documentos válidos em um banco de dados SQLite e permite visualizar os documentos cadastrados.

Funcionalidades
Validação de CPF e CNPJ com base nos algoritmos oficiais.

Formatação correta dos números validados.

Armazenamento dos CPFs/CNPJs válidos em banco de dados SQLite.

Evita armazenamento duplicado.

Interface web simples para envio e validação dos documentos.

Possibilidade de consultar todos os documentos armazenados.

Permite múltiplas validações em sequência até o usuário decidir sair.

Tecnologias utilizadas
Python 3

Flask (framework web)

SQLite (banco de dados leve)

HTML (formulário para entrada dos dados)

Regex (para limpeza dos documentos)

Estrutura do Projeto
app.py - Aplicação principal Flask, gerencia rotas e interações web.

validator.py - Funções para limpar, validar e formatar CPF e CNPJ.

init_db.py - Script para inicializar o banco de dados SQLite.

templates/form.html - Formulário HTML para entrada de CPF/CNPJ.

documentos.db - Banco de dados SQLite (gerado após rodar o projeto).

.gitignore - Arquivos e pastas ignorados pelo Git.

requirements.txt - Lista de dependências Python (ex: Flask).

Como usar
Pré-requisitos
Python 3 instalado

Ambiente virtual recomendado (ex: venv)

Passos
Clone o repositório:

bash
Copiar
Editar
git clone <URL-do-repositório>
cd <nome-do-projeto>
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Inicialize o banco de dados (execute uma vez):

bash
Copiar
Editar
python init_db.py
Execute a aplicação:

bash
Copiar
Editar
python app.py
Acesse a aplicação no navegador:

cpp
Copiar
Editar
http://127.0.0.1:5000/
Uso
Selecione o tipo de documento (CPF ou CNPJ).

Digite o número e envie.

A aplicação mostrará se o documento é válido ou inválido.

Você pode escolher validar outros documentos ou visualizar todos os documentos armazenados.

Mensagens
"CPF inválido!" — CPF não passou na validação oficial.

"CNPJ inválido!" — CNPJ não passou na validação oficial.

"CPF salvo com sucesso: XXX.XXX.XXX-XX" — CPF válido e salvo no banco.

"CNPJ salvo com sucesso: XX.XXX.XXX/XXXX-XX" — CNPJ válido e salvo no banco.

"CPF/CNPJ já está armazenado" — Documento já cadastrado.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correções ou novas funcionalidades.

Licença
Este projeto está sob a licença MIT — veja o arquivo LICENSE para detalhes.

Autor
Hadriely Harrizon
