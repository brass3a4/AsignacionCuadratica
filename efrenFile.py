import itertools
import string


#Parametros: [lista cromosoma, int n, arreglo 2D matrizA, arreglo 2D matrizB]
def calcularAptitud(cromosoma, n, matrizA, matrizB):
	#Definicion del diccionario que usare para saber las posiciones de la permutacion
	alfabeto = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":6, "H":6, "I":6, "J":6, "K":6, "L":6, "M":6, "N":6, "O":6, "P":6,
	 "Q":6, "R":6, "S":6, "T":6, "U":6, "V":6, "W":6, "X":6, "Y":6,resultado }
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