#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
from libj import *

def factorial(n):
	max=1 
	if(n>0): 
		max=factorial(n-1)  
		max=max*n  
	else:  
		max=1 
	return max 

#genera la poblacion con el numero de elementos que se solicitan
#parametros: poblacion es la poblacion total, cantidad es el numero de elementos que vamos a tomar de la poblacion
#devuelve la generacion que contiene el numero de elementos solicitados

def tomarGeneracion(poblacion,cantidad):
	generacion=[]
	numeros=[]
	min=1
	max=factorial(cantidad)
	if(max < min):
		print"error"
		min, max = max, min
	if(cantidad > (max-min)):
		print "error: solicita mas elementos de los que tiene"
		cantidad = max - min
	while len(numeros) < cantidad:
		numero=random.randint(min, max)
		if numero in numeros:
			numero=random.randint(min, max)
		else:
			numeros.append(numero)
	for i in range(0,cantidad):
		generacion.append(poblacion[numeros[i]-1])
	return generacion



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
	Z[0] = 	random.randrange(1000000)
	for i in range(1, m+1):
		Z[i]=(a*Z[i-1]) % denom
	for i in range (1,m+1):
		aleatoriosDecimales[i]=round((Z[i]/denom),6)
	return aleatoriosDecimales  
 
	

#funcion para mutar los cromosomas seleccionados, aplicando el metodo dos de mutacion
#recibe: lista de cromosomas que van a mutar
#devuelve: lista de cromosomas mutados

def mutSec(elemento,operadores):
	elem_mutado=elemento
	mut1=operadores[0]
	mut2=operadores[1]
	aux=elemento[mut1-1:mut2]
	aux2=aux[::-1]
	for i in range (0,len(elemento)):
		if (i == mut1):
			for j in range (0, len(aux2)):
				elem_mutado[i-1]=aux2[j]
				i=i+1
	return elem_mutado
	
#mutacion primaria del cromosoma (intercambio de la posicion seleccionada del cromosoma)
def mutPrim(elemento, operadores):
	fin=[]
	lim=len(elemento)
	for k in range (0,len(operadores)):
		fin.append(elemento[operadores[k]-1])
		p = fin[::-1]
		for c in range(0,len(p)):
			elemento[operadores[c]-1]=p[c]
	return elemento



#ver que posicion muta el cromosoma
#parametros: w tamaño del cromosoma
def generadorEnt(w,cantidad):
	operadores=[]
	#selecciona dos elementos del cromosoma seleccionado
	while len(operadores) < cantidad:
		numero = random.randint(1,6)
		if numero in operadores:
			numero = random.randint(1,6)
		else:
			operadores.append(numero)
	if(operadores[0]>operadores[1]):
		aux=operadores[0]
		operadores[0]=operadores[1]
		operadores[1]=aux
	return operadores
	
#funcion muta recibe cromosomas que es una lista de cromosomas que van a mutar generada por la muncion selCrom
def muta(cromosomas):
	cromosomas_mutados=[]
	cantidad=2 #numero de elementos a mmutar

	#lee un cromosoma y aplica mutacion en las posiciones definidas
	for i in range(0,len(cromosomas)):
		elemento=cromosomas[i]
		w=len(elemento)
		#llama a la funcion 
		operadores=generadorEnt(w,cantidad)
		elemento_mutado=mutPrim(elemento, operadores)
		cromosomas_mutados.append(elemento_mutado)
	return cromosomas_mutados
	
#comparando con pm, selecciona los elementos de la muestra que van a mutar
def mutar(muestraPob,pm):
	muestrachida = []
	for k in xrange(0, len(muestraPob)):
		muestrachida.append(list(muestraPob[k]))
	cromosomas=[]
	b_pos=[]
	#generacion_mutada=[]
	a=generaAleatDec(len(muestraPob))
	#a=[0.5,0.4,0.3,0.7]
	#selecciona los elementos de la muestra que van a mutar
	for i in range(1,len(a)):
		if (a[i] < pm):
			b_pos.append(i+1)
	for i in range (0,len(b_pos)):
		cromosomas.append(muestrachida[b_pos[i]-1])
	generacion_mutada=muta(cromosomas)
	return generacion_mutada