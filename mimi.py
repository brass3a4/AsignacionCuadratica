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
#genera la poblacion con el numero de elementos que se solicitan
#parametros: poblacion es la poblacion total, cantidad es el numero de elementos que vamos a tomar de la poblacion
#devuelve la generacion que contiene el numero de elementos solicitados
def tomarGeneracion(poblacion,cantidad):
	numeros=[]
	generacion=[]
	min=1
	#define el limite superior para generar la poblacion inicial
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
	for i in range(1,cantidad+1):
		generacion[i]=poblacion[numeros[i]]
	return generacion



#funcion genera numeros aleatorios [0,1]
#funcion: Zi=(a*Zi-1) mod m
#parametros: modulo m, el multiplicador a y la semilla o valor de comienzo Z0 son enteros no negativos
#se verifica que:0 menor o igual que Zi menor que m
#Para obtener un numero aleatorio de la distribucion uniforme [0,1) se debe hacer Ui = Zi/m. Además de ser no negativos se debe veriﬁcar que: 0 < m, a < m, c < m, Z0 < m
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

