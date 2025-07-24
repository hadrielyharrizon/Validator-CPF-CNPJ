'''
CPF and CNPJ Validator

This script allows you to validate CPF and CNPJ numbers
based on the official rules for verifying digits.

Author: Hadriely Harrizon
'''

print ("Validação de CPF/CNPJ");
doc_type = input ("CPF - 1 | CNPJ - 2: ");

if doc_type == "1":
    doc = input("Digite o CPF: ")
elif doc_type == "2":
    doc = input("Digite o CNPJ: ")
else:
    print("Opção Inválida.")

def clean_doc(doc):
    return ''.join(filter(str.isdigit, doc))

documento_limpo = clean_doc(doc)
print("Documento limpo:", documento_limpo)
