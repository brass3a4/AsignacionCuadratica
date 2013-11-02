# -*- encoding: utf-8 -*-
import random
import itertools
def eligeCemilla():
	while(1):
		num=random.randrange(1000000)
		contador = 0
		verificar= False
		for i in range(1,num+1):
			if (num% i)==0:
				contador = contador + 1
			if contador >= 3:
				verificar=True
				break
		if contador==2 or verificar==False:
			primo=num
			return primo

def generaAleatDec(m):
	Z={}
	aleatoriosDecimales={}
	denom= (pow(2,31))-1.0
	a = 630360016
	Z[0] = 	eligeCemilla()
	for i in range(1, m+1):
		Z[i]=(a*Z[i-1]) % denom
	for i in range (1,m+1):
		aleatoriosDecimales[i]=round((Z[i]/denom),6)
	aleatoriosDecimales[0]=round(Z[0]/denom,6)
	return aleatoriosDecimales

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
	numeros = generaAleatDec(10)
	Q = [0.0,0.3,0.6,1.0]
	elementos = []
	print numeros
	for i in xrange(1,len(generacion)+1):
		for qi in xrange(0, len(Q)):
			if numeros[i] <= Q[qi]:				
				elementos.append(generacion[qi])
				break

	return elementos

def seleccionarElementosCruce(elementos,pc):
	numeros2 = generaAleatDec(10)
	elementosCruce = []

	for j in xrange(1, len(elementos)+1):
		if numeros2[j] > pc:
			elementosCruce.append(elementos[j-1])

	return elementosCruce

def traerElementosCruce(elementos,pc):
	elementosCruce = seleccionarElementosCruce(elementos,pc)
	while (len(elementosCruce)%2) !=0 or len(elementosCruce) == 0:
		elementosCruce = seleccionarElementosCruce(elementos,pc)
	return elementosCruce

# generacion = [('C', 'A', 'D', 'B'), ('B', 'A', 'D', 'C'), ('B', 'D', 'C', 'A'), ('D', 'C', 'A', 'B')]
# elementos = ruleta(generacion)
# print elementos
# elementosCruce = traerElementosCruce(elementos,0.5)
# print elementosCruce


