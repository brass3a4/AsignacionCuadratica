#!/usr/bin/env python	
# -*- coding: utf-8 -*-


#archivo_matriz_A= "/home/shangueili/Escritorio/algoritmos_proyecto/matrizA.txt"
#archivo_matriz_B= "/home/shangueili/Escritorio/algoritmos_proyecto/matrizB.txt"

def cargarMatriz(archivo):
	f = open(archivo)
	data = f.read().strip()
	f.close
	M= [[int(num) for num in line.strip().split()] for line in data.split('\n')]
	return M
	

def obtenerElemMatriz(matriz,p,q):
	if (matriz == 'A'):
		n = CargarMatriz(archivo_matriz_A)
		for i in range(0, len(n)):
			for j in range(0,len(n)):
				if (p==i and q==j):
					res = n[i][j]
		return res
	elif (matriz =='B'):
		n = CargarMatriz(archivo_matriz_B)
		for i in range(0, len(n)):
			for j in range(0,len(n)):
				if (p==i and q==j):
					res = n[i][j]
		return res
