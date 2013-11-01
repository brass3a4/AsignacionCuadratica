# -*- encoding: utf-8 -*-

# Importamos las liberias del proyecto
from libj import *

# Definimos las probabilidades
# pc := Probablilidad de cruce
# pm := Probabilidad de mutación

pc = 0.5
pm = 0.1


def principal():

	print generarPoblacion(5)

principal()