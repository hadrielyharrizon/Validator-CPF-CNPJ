'''
CPF and CNPJ Validator

This script allows you to validate CPF and CNPJ numbers
based on the official rules for verifying digits.

Author: Hadriely Harrizon
'''

import re

def clean_doc(numero):
    return re.sub(r'\D', '', numero)

def validar_cpf(cpf):
    cpf = clean_doc(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True

def validar_cnpj(cnpj):
    cnpj = clean_doc(cnpj)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    def calc_digito(pesos, n):
        soma = sum(int(n[i]) * pesos[i] for i in range(len(pesos)))
        digito = soma % 11
        return '0' if digito < 2 else str(11 - digito)

    dig1 = calc_digito(pesos1, cnpj)
    dig2 = calc_digito(pesos2, cnpj + dig1)

    return cnpj[-2:] == dig1 + dig2

def formatcpf(cpf):
    cpf = clean_doc(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formatcnpj(cnpj):
    cnpj = clean_doc(cnpj)
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
