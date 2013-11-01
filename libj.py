# -*- encoding: utf-8 -*-

import itertools

# Descripción: Esta función genera las n permutaciones 
# Parametros: [int n]
def generarPoblacion(n):

	#Definicion del diccionario que usare para saber las posiciones de la permutación
	alfabeto = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P",17:"Q", 19:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
	lista = []

	# Creo una lista de n elementos a permutar
	for elemento in xrange(1,n+1):
		lista.append(alfabeto[elemento])
	
	# Creo una lista con todas las n permutaciones
	poblacion = list(itertools.permutations(lista))

	return poblacion
