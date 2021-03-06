# -*- encoding: utf-8 -*-
import random
import itertools
from efrenFile import *

#funcion genera numeros aleatorios [0,1]
#funcion: Zi=(a*Zi-1) mod m
#parametros: modulo m, el multiplicador a y la semilla o valor de comienzo Z0 son enteros no negativos
#se verifica que:0 menor o igual que Zi menor que m
#Para obtener un numero aleatorio de la distribucion uniforme [0,1) se debe hacer Ui = Zi/m. Además de ser no negativos se debe veriﬁcar que: 0 < m, a < m, c < m, Z0 < m
def generaAleatDec(m):
	Z={}
	aleatoriosDecimales={}
	denom= (pow(2,31))-1.0
	a = 630360016
	Z[0] = 	random.randrange(10)
	for i in range(1, m+1):
		Z[i]=(a*Z[i-1]) % denom
	for i in range (1,m+1):
		aleatoriosDecimales[i]=round((Z[i]/denom),6)
	return aleatoriosDecimales  

# Descripción: Esta función genera las n permutaciones 
# Parametros: [int n]
def generarPoblacion(n):

	#Definicion del diccionario que usare para saber las posiciones de la permutación
	alfabeto = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P",17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}
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

# Descripción: Selecciona los cromosomas candidatos a cruce dependiendo de la probailidad acumulada Q
# Parámetros: [list generacion, list Q]
def ruleta(generacion,Q,cardinalidadGeneracion):

	elementos = []
	tam= len(Q)
	# Desde 1 hasta el tamaño de la generación
	for cromosoma in generacion:
		numeros = generaAleatDec(1)
		
		# Desde 0 hasta el tamaño de Q
		for qi in xrange(1,tam):
			
			# Si el Q[qi] correspondiente es <= al número aleatorio seleccionamos al cromosoma Q[qi] como candidato a cruce
			if numeros[1] < Q[qi]:				
				elementos.append(generacion[qi-1])
				break
			
	return elementos

# Descripción: Selecciona cromosomas a cruzar dependiendo de la probabilidad de cruce
# Parámetros: [list elementos,float pc]
def seleccionarElementosCruce(elementos,pc):
	# Obtengo números aleatorios
	numeros2 = generaAleatDec(10)
	
	elementosCruce = []
	j=1
	# Para cada número aleatorio que sea mayor a la PC Agrego el cromosoma correspondiente a la lista de elementos a cruzar
	for cromosoma in elementos:
		if numeros2[j] < pc:
			elementosCruce.append(cromosoma)
		j = j+1	
			
	return elementosCruce

# Descripción: Mientras no tenga un número PAR de cromosomas selecciono cromosomas
# Parámetros: [list elementos,float pc]
def traerElementosCruce(elementos,pc,cardinalidadGeneracion):
	
	elementosCruce = seleccionarElementosCruce(elementos,pc)
	if (len(elementosCruce)%2 != 0):
		elementos.pop()
	
	return elementosCruce

# Descripción: Cruzamos un número PAR de cromosomas
# Parámetros: [list cromosomas, int n, list matrizA, list matrizB]
def cruzarCromosomas(cromosomas,n,matrizA,matrizB):
	hijo = []
	entran = []
	salen = []
	if len(cromosomas)%2 == 0:
		for i in xrange(0,len(cromosomas),2):
			# Tomamos los primeros 2 cromosomas a cruzar
			papa = cromosomas.pop()
			mama = cromosomas.pop()
			# Hacemos el algoritmo de cruce
			for j in xrange(1, len(papa)):
				if not(papa[0] in hijo): # Colocamos el primer Gen en el hijo
					hijo.append(papa[0])
				if j <= len(papa):
					if not(mama[j] in hijo): #Tomamos el Gen j del segundo cromosoma y lo ponemos en el hijo
				 		hijo.append(mama[j])
			for letra in xrange(0,len(papa)): # Si nos falto un Gen en el hijo colo camos el elemento que nos falta
				if not(papa[letra] in hijo):
					hijo.append(papa[letra])
			# Calculamos las aptitudes de los cromosomas 
			aptitudPapa = calcularAptitud(papa, n, matrizA, matrizB)
			aptitudMama = calcularAptitud(mama, n, matrizA, matrizB)
			# Nos quedamos con el cromosoma de mayor aptitud y el hijo (Cromosoma resultante de la cruza)
			if aptitudPapa < aptitudMama:
				salen.append(mama)
				if not(hijo in entran):
					entran.append(hijo)
			else:
				salen.append(papa)
				if not(hijo in entran):
					entran.append(hijo)

	nuevosCromosomas = {"entran":entran, "salen": salen}

	if(len(nuevosCromosomas['salen']) > len(nuevosCromosomas['entran'])):
		nuevosCromosomas['salen'].pop()

	return nuevosCromosomas