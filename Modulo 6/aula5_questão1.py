# -*- coding: utf-8 -*-
"""Aula5_Questão1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UX8SC-shQ9GZwmHkrvFmqfHcvrpm0aRQ
"""

import math

raios = [1.5, 0.8, 2.3, 5.0]

calcula_area = lambda r: round(math.pi * (r ** 2), 2)

areas = list(map(calcula_area, raios))

print(areas)