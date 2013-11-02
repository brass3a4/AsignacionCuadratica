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
	return matriz[p][q]
	#for i in range(1, 1 + len(matriz)):
	#	for j in range(1, 1 + len(matriz)):
	#		if (p==i and q==j):
	#			res = matriz[i][j]
	#			return res
	
