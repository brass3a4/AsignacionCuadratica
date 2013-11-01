# -*- encoding: utf-8 -*-

import itertools

# Descripción: Esta función genera las n permutaciones 
# Parametros: [int n]
def generarPoblacion(n):
	lista = []
	# Creo una lista de n elementos a permutar
	for elemento in xrange(1,n+1):
		lista.append(elemento)

	# Creo una lista con todas las n permutaciones
	poblacion = list(itertools.permutations(lista))

	return poblacion
