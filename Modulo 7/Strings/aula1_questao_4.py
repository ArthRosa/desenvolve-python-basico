# -*- coding: utf-8 -*-
"""aula1_questao 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
numero = input("Digite o número: ")

# processamento
if len(numero) == 8:
    numero_completo = "9" + numero
elif len(numero) == 9:
    if numero[0] == '9':
        numero_completo = numero[:5] + "-" + numero[5:]
    else:
        numero_completo = numero[:5] + "-" + numero[5:]
else:
    print("Número inválido. Por favor, insira um número de telefone válido.")

# saida
print(f"Número completo: {numero_completo}")