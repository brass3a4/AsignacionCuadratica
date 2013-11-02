#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
gen =[]
b=[]
b_pos=[]
mutar = []
#a=[0.5,0.4,0.3,0.7,0.9,0.6,0.4,0.3,0.4]
#pm = 0.5
#cromosoma =['A','B','C','D','E','F']

#agarrar decimales del tamaño de la poblacion (genera n numeros aleatorios)
a = generaAleatDec(m,primo)

#comparando con pm 
def selCrom(a, pm):
	for i in range(0,len(a)):
		if (a[i] < pm):
			b.append(a[i])	
			b_pos.append(i)
	return b
	
#w tamaño del cromosoma
#ver que posicion muta el cromosoma
def generadorEnt(w):
	for i in range(0,2):
		number_random_int = random.randint(1,w)
		gen.append(number_random_int)
	return gen

#mutacion primaria del cromosoma (intercambio de la posicion seleccionada del cromosoma)
def mutPrim(cromosoma, gen):
	print "MUTACION"
	print cromosoma
	for i in range(0,len(gen)):
		mutar.append(cromosoma[gen[i]])
		p = mutar[::-1]  
		for i in range(0, len(p)):
			cromosoma[gen[i]] = p[i]
	return cromosoma

seleccion=selCrom(a,pm)
generadores = generadorEnt(len(seleccion))
print mutPrim(cromosoma,generadores)
		
	

	
	
	
	
		
