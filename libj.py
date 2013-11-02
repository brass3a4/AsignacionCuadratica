# -*- encoding: utf-8 -*-

import itertools

def generaAleatDec(m,primo):
	Z={}
	U={}
	denom= (pow(2,31))-1.0
	a = 630360016
	Z[0] = primo
	for i in range(1, m+1):
		Z[i]=(a*Z[i-1]) % denom
	for i in range (1,m+1):
		U[i]=round((Z[i]/denom),3)
	U[0]=round(Z[0]/denom,3)
	return U

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

# Elementos de entrada: Generación i
# Elementos de salida: Generacion i+1 (Cruzada)
# Tomo numeros aleatorios
# Ruleta 
# - Definimos una nueva poblacion Vi de tamaño m
# - Generas nuevos numeros aleatorios cambiando la semilla (primo)
# - Comparas los numeros aleatorios con pc y elijo los cromosomas que van a cruzar
# - Cruza
# - Quito el menos apto

def ruleta(generacion):
	numeros = generaAleatDec(10,232435)
	q0 = 0.3
	q1 = 0.6
	q2 = 0.8
	q3 = 1
	elementos = []
	for i in xrange(1,len(generacion)+1):
		if numeros[i] < q0 :
			elementos.append(generacion[0])
		elif numeros[i] > q0 and numeros[i] <= q1:
			elementos.append(generacion[1])
		elif numeros[i] > q1 and numeros[i] <= q2:
			elementos.append(generacion[2])
		elif numeros[i] > q2 and numeros[i] <= q3:
			elementos.append(generacion[3])

	return elementos

def seleccionarElementosCruce(elementos,pc):
	numeros2 = generaAleatDec(10,232)
	elementosCruce = []

	for j in xrange(1, len(elementos)+1):
		if numeros2[j] > pc:
			elementosCruce.append(elementos[j-1])

	return elementosCruce

generacion = [('C', 'A', 'D', 'B'), ('B', 'A', 'D', 'C'), ('B', 'D', 'C', 'A'), ('D', 'C', 'A', 'B')]
elementos = ruleta(generacion)
print elementos
elementosCruce = seleccionarElementosCruce(elementos,0.5)
print elementosCruce