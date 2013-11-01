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
	
		
#print CargarMatriz(archivo_matriz_A)
#print CargarMatriz(archivo_matriz_B)
