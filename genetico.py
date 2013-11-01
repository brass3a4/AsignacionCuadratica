# -*- encoding: utf-8 -*-

# Importamos las liberias del proyecto
from libj import *
from mimi import *
from efrenFile import *
from beatriz import *


# Definimos las probabilidades
# pc := Probablilidad de cruce
# pm := Probabilidad de mutación

pc = 0.5
pm = 0.1

# n:= Tamaño del cromosoma
n = 4

def principal():
	poblacion = generarPoblacion(n)
	matrizA = cargarMatriz('matrizA.txt')
	matrizB = cargarMatriz('matrizB.txt')
	generacion = tomarGeneracion(poblacion,n)

principal()
