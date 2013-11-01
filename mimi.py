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


