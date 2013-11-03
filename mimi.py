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



#funcion para mutar los cromosomas seleccionados, aplicando el metodo dos de mutacion
#recibe: lista de cromosomas que van a mutar
#devuelve: lista de cromosomas mutados


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
	w=len(cromosomas[0])
	cantidad=2 #numero de elementos a mmutar
	#llama a la funcion 
	operadores=generadorEnt(w,cantidad)
	#lee un cromosoma y aplica mutacion en las posiciones definidas
	for i in range(0,len(cromosomas)):
		elemento=cromosomas[i]
		elemento_mutado=mutPrim(elemento, operadores)
		cromosomas_mutados.append(elemento_mutado)
	return cromosomas_mutados
	
#comparando con pm, selecciona los elementos de la muestra que van a mutar
def mutar(muestraPob,pm):
	cromosomas=[]
	b_pos=[]
	#generacion_mutada=[]
	a=generaAleatDec(len(muestraPob))
	#selecciona los elementos de la muestra que van a mutar
	for i in range(0,len(a)):
		if (a[i] < pm):
			b_pos.append(i+1)
	for i in range (0,len(b_pos)):
		cromosomas.append(muestraPob[b_pos[i]-1])
	generacion_mutada=muta(cromosomas)
	return generacion_mutada