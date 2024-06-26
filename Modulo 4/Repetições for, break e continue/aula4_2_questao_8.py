# -*- coding: utf-8 -*-
"""aula4.2_questao 8

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
resultado = 0
operador = '+'  # Inicialmente, o operador é '+'

# Loop para ler os valores e operadores até que o usuário digite "Fim"
while True:
    entrada = input().strip()  # Leitura da entrada e remoçao de espaços em branco

    if entrada == "Fim":
        break  # Encerra o loop quando o usuário digitar "Fim"

    if entrada == '+' or entrada == '-':
        operador = entrada  # Atualiza o operador

    else:
        valor = int(entrada)
        if operador == '+':
            resultado += valor
        elif operador == '-':
            resultado -= valor

# saida
print(resultado)