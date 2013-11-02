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

	# Generamos la población
	poblacion = generarPoblacion(n)
	# Leemos las matrices A y B que están en los ficheros
	matrizA = cargarMatriz('matrizA.txt')
	matrizB = cargarMatriz('matrizB.txt')
	# Tomamos la generación cero de la población total
	generacion = tomarGeneracion(poblacion,n)

	# Calculamos la aptitud de cada cromosoma
	for cromosoma in generacion:
		print calcularAptitud(cromosoma, n, matrizA, matrizB)

principal()
