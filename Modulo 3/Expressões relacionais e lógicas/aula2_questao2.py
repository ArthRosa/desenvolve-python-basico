# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

# entrada
idade_juliana = int(input("Digite a idade de Juliana: "))

idade_cris = int(input("Digite a idade de Cris: "))

#processando
podem_entrar = idade_juliana > 17 or idade_cris > 17

# saida
if podem_entrar:
    print(True)
    print("Juliana e Cris podem entrar no bar.")
else:
    print(False)
    print("Juliana e Cris não podem entrar no bar.")