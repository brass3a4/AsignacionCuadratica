# -*- encoding: utf-8 -*-

# Importamos las liberias del proyecto
from libj import *
from mimi import *
from efrenFile import *
from beatriz import *
import sys
import os

# Validamos el número de argumentos para ejecutar el programa
if len(sys.argv) != 5:
	print "$ python genetico.py [Tamaño de cromosoma] [Cardinalidad de la generación] [Probabilidad de cruce] [Probabilidad de mutación]"
	sys.exit('No coicide el número de argumentos') 

# n:= Tamaño del cromosoma
n = int(sys.argv[1])
#  cardinalidadGeneracion := Cardinalidad de la generación
cardinalidadGeneracion = int(sys.argv[2])

# Definimos las probabilidades
# pc := Probablilidad de cruce
# pm := Probabilidad de mutación

pc = float(sys.argv[3])
pm = float(sys.argv[4])

# Limpiamos pantalla antes de iniciar
#os.system("clear")

def principal():
	bandera = 0
	aptitudCromosomasMasApto = 0
	sumaAptitudes = 0
	cromosomaMasApto = ""
	# Generamos la población
	poblacion = generarPoblacion(n)

	# Leemos las matrices A y B que están en los ficheros
	matrizA = cargarMatriz('matrizA2.txt')
	matrizB = cargarMatriz('matrizB2.txt')
	# Tomamos la generación cero de la población total
	generacion = tomarGeneracion(poblacion,cardinalidadGeneracion)
	#print "generacion"
	original = generacion [:]
	#print generacion

	for iteracion in xrange(1,100):
		if bandera > 0:
			generacion = siguienteGeneracion[:]

		aptitudesGeneracion = []
		
		# Calculamos la aptitud de cada cromosoma
		for cromosoma in generacion:
			aptitudCromosomaAnalizado = calcularAptitud(cromosoma, n, matrizA, matrizB)
			aptitudesGeneracion.append(aptitudCromosomaAnalizado)
			if aptitudCromosomaAnalizado < aptitudCromosomasMasApto:
				aptitudCromosomasMasApto = aptitudCromosomaAnalizado
				cromosomaMasApto = cromosoma
			sumaAptitudes = sumaAptitudes + aptitudCromosomaAnalizado
		probabilidadesUnitarias = calcularProbabilidadUnitaria(aptitudesGeneracion, sumaAptitudes)
		probabilidadesAcumuladas = calcularProbabilidadAcumulada(probabilidadesUnitarias)
		
		cromosomasRuleta = ruleta(generacion,probabilidadesAcumuladas,cardinalidadGeneracion)
		#print "cromosomasRuleta"
		#print cromosomasRuleta
		cromosomasACruzar = traerElementosCruce(cromosomasRuleta,pc,cardinalidadGeneracion) 
		#print "cromosomas a cruzar"
		#print cromosomasACruzar
		nuevosCromosomas =cruzarCromosomas(cromosomasACruzar,n,matrizA,matrizB)
		#print nuevosCromosomas

		for salen in nuevosCromosomas['salen']:
			if (salen in generacion):
				generacion.remove(salen)
		for entran in nuevosCromosomas['entran']:
			generacion.append(entran)
		#print "Nueva Generacion"
		#print generacion
		
		#nuevosCromosomas = generacion
		#cromosomasMutados = mutar(nuevosCromosomas,pm)
		#print cromosomasMutados
		

		aptitudesNuevaGeneracion = []
		sumaAptitudesNuevas = 0
		
		siguienteGeneracion = mutarGeneracionCruzada(generacion, pm, n)
		bandera = bandera + 1
		for nuevoCromosoma in siguienteGeneracion:
			aptitudNuevoCromosomaAnalizado = calcularAptitud(nuevoCromosoma, n, matrizA, matrizB)
			aptitudesNuevaGeneracion.append(aptitudNuevoCromosomaAnalizado)
			if aptitudNuevoCromosomaAnalizado < aptitudCromosomasMasApto:
				aptitudCromosomasMasApto = aptitudNuevoCromosomaAnalizado
				cromosomaMasApto = nuevoCromosoma
			sumaAptitudesNuevas = sumaAptitudesNuevas + aptitudNuevoCromosomaAnalizado
		print "|"
		os.system("clear")
		print "-"
		os.system("clear")
	
	print "Aptitud inicial:",sumaAptitudes
	print "Aptitud final:",sumaAptitudesNuevas
	if sumaAptitudesNuevas < sumaAptitudes:
		print "Mejoro con respecto la generacion anterior"
	else:
		print "No mejoro con respecto a la generacion anterior"
	print "***************"
	print "Generiacion 0"
	for cromosoma in original:
		print cromosoma
	print "Generacion despues de la cruza"
	for cromosoma in generacion:
		print cromosoma
	print "Ultima generacion"
	for cromosoma in siguienteGeneracion:
		print cromosoma
	print bandera

principal()
