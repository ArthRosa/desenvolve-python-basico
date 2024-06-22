# -*- coding: utf-8 -*-
"""aula4.2_questao4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# Lista para armazenar os 10 números digitados pelo usuário
numeros = []

# Solicita ao usuário para inserir 10 números positivos
print("Digite 10 números positivos:")
for i in range(10):
    numero = int(input())
    while numero <= 0:
        print("O número deve ser positivo. Tente novamente.")
        numero = int(input())
    numeros.append(numero)

# Calcula a média dos números digitados
media = sum(numeros) / len(numeros)

# Imprime a média com duas casas decimais
print(f"A média dos valores digitados é {media:.2f}")