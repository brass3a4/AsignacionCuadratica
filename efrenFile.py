import itertools
import string

from beatriz import *


#Parametros: [lista cromosoma, int n, arreglo 2D matrizA, arreglo 2D matrizB]
def calcularAptitud(cromosoma, n, matrizA, matrizB):
	#Definicion del diccionario que usare para saber las posiciones de la permutacion
	alfabeto = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16,
	 "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
	 #en esta variable se guardara el resultado de la aptitud del cromosoma
	resultadoAptitud = 0
	 #Recorro cada elemeto de la matriz a para multiplicarlo con la permutacion del cromosoma en b
	for columna in xrange(1,n):
		for renglon in xrange(1,n):
	 		elementoA = obtenerElemMatriz(matrizA, columna, renglon)
	 		valorI = cromosoma[columna]
	 		valorK = cromosoma[renglon]
	 		elementoB = obtenerElemMatriz(matrizB, alfabeto[valorI], alfabeto[valorK])
	 		producto = elementoA * elementoB
	 		resultadoAptitud = resultadoAptitud + producto
	return resultadoAptitud