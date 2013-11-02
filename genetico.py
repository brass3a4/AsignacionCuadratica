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
	aptitudCromosomasMasApto = 0
	sumaAptitudes = 0
	cromosomaMasApto = ""
	# Generamos la población
	poblacion = generarPoblacion(n)
	# Leemos las matrices A y B que están en los ficheros
	matrizA = cargarMatriz('matrizA.txt')
	matrizB = cargarMatriz('matrizB.txt')
	# Tomamos la generación cero de la población total
	generacion = tomarGeneracion(poblacion,n)
	aptitudesGeneracion = []

	# Calculamos la aptitud de cada cromosoma
	for cromosoma in generacion:
		aptitudCromosomaAnalizado = calcularAptitud(cromosoma, n, matrizA, matrizB)
		aptitudesGeneracion.append(aptitudCromosomaAnalizado)
		if aptitudCromosomaAnalizado < aptitudCromosomasMasApto:
			aptitudCromosomasMasApto = aptitudCromosomaAnalizado
			cromosomaMasApto = cromosoma
		sumaAptitudes = sumaAptitudes + aptitudCromosomaAnalizado
	probabilidadesUnitarias = calcularProbabilidadUnitaria(aptitudesGeneracion, sumaAptitudes)
	probabilidadesAcumuladas = calcularProbabilidadAcumulada(probabilidadesUnitarias)

	cromosomasRuleta = ruleta(generacion,probabilidadesAcumuladas)
	cromosomasACruzar = traerElementosCruce(cromosomasRuleta,pc) 
	print cromosomasACruzar

principal()
