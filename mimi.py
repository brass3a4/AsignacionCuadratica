#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
from libj import *


m=10
min=1
max=1
#calcula factorial como limite superior para generar los m cromosomas de la generacion
def factorial(max,n):  
	if(n>0):  
		max=factorial(max,n-1)  
		max=max*n  
	else:  
		max=1  
	return max  


#Descripción: funcion para elegir los elementos de la primera generacion sin repeticion
#Parametros: int m es el numero de elementos, int min el limite inferior e int max el limite superior.
def aleatorios(cantidad, min, max):
	#print "hola"
    numeros = set()
    if(max < min):
        min, max = max, min
    #valida que no se pidan mas elementos del rango de seleccion   
    if(cantidad > (max-min)):
        cantidad = max - min
    while len(numeros) < cantidad:
        numeros.add(random.randint(min, max))
    return numeros


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

