# -*- coding: utf-8 -*-
"""Aula4_Questão4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UX8SC-shQ9GZwmHkrvFmqfHcvrpm0aRQ
"""

alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

for aluno in aprovados:
    print(aluno)