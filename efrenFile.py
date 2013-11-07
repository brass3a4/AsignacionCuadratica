import itertools
import string
import ast
import random

from beatriz import *
from mimi import *


#Parametros: [lista cromosoma, int n, arreglo 2D matrizA, arreglo 2D matrizB]
def calcularAptitud(cromosoma, n, matrizA, matrizB):
	#Definicion del diccionario que usare para saber las posiciones de la permutacion
	alfabeto = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16,
	 "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
	 #en esta variable se guardara el resultado de la aptitud del cromosoma
	resultadoAptitud = 0
	 #Recorro cada elemeto de la matriz a para multiplicarlo con la permutacion del cromosoma en b
	for columna in xrange(0, n):
		for renglon in xrange(0, n):
			elementoA = obtenerElemMatriz(matrizA, renglon, columna)
			valorI = cromosoma[columna]
			valorI = alfabeto[valorI]
			valorI = -1 + int(valorI)
			valorK = cromosoma[renglon]
			valorK = alfabeto[valorK]
			valorK = -1 + int(valorK)
	 		elementoB = obtenerElemMatriz(matrizB, valorI, valorK)
	  		producto = elementoA * elementoB
	  		resultadoAptitud = resultadoAptitud + producto
	return resultadoAptitud

def calcularProbabilidadUnitaria(aptitudesGeneracion, sumaAptitudes):
	probabilidadesUnitarias = []
	for indice in xrange(0, len(aptitudesGeneracion)):
		probabilidadesUnitarias.append(float(aptitudesGeneracion[indice])/float(sumaAptitudes))
	return probabilidadesUnitarias

def calcularProbabilidadAcumulada(probabilidadesUnitarias):
	sumaAcumulada = 0
	probabilidadesAcumuladas = [0]
	for indice in xrange(0,len(probabilidadesUnitarias)):
		sumaAcumulada = sumaAcumulada + probabilidadesUnitarias[indice]
		if indice == -1 + len(probabilidadesUnitarias):
			sumaAcumulada = round(sumaAcumulada)
		probabilidadesAcumuladas.append(sumaAcumulada)
	return probabilidadesAcumuladas

def mutarGeneracionCruzada(nuevosCromosomas, pm, n):
	resultadoMutacion = []
	for cromosoma in nuevosCromosomas:
		cromosoma = list(cromosoma)
		marcaA = random.randrange(n)
		marcaB = random.randrange(n)
		while marcaA == marcaB:
			marcaB = random.randrange(n)
		numDecAleat = generaAleatDec(1)
		num = numDecAleat.get(1)
		#print num
		if num < pm:
			aux = cromosoma[marcaA]
			cromosoma[marcaA] = cromosoma[marcaB]
			cromosoma[marcaB] = aux
		cromosoma = tuple(cromosoma)
		resultadoMutacion.append(cromosoma)
	return resultadoMutacion

def crearPrimeraGeneracion(n):
	alfabeto = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P",17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}

	generacion = []
	cromosoma = []
	for x in xrange(1,n+1):
		cromosoma.append(alfabeto[x]);
	
	for y in xrange(1,n+1):
		random.shuffle(cromosoma)
		#print cromosoma
		generacion.append(tuple(cromosoma))
	
	return generacion