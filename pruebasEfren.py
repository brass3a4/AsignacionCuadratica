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
os.system("clear")

def principal():
	aptitudCromosomasMasApto = 0
	sumaAptitudes = 0
	cromosomaMasApto = ""
	# Generamos la población
	poblacion = generarPoblacion(n)
	# Leemos las matrices A y B que están en los ficheros
	matrizA = cargarMatriz('matrizA.txt')
	matrizB = cargarMatriz('matrizB.txt')
	# Tomamos la generación cero de la población total
	generacion = tomarGeneracion(poblacion,cardinalidadGeneracion)
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

	cromosomasRuleta = ruleta(generacion,probabilidadesAcumuladas)
	#print cromosomasRuleta
	cromosomasACruzar = traerElementosCruce(cromosomasRuleta,pc) 
	#print cromosomasACruzar
	nuevosCromosomas =cruzarCromosomas(cromosomasACruzar,n,matrizA,matrizB)
	
	# ********************************************************************
	aptitudesNuevaGeneracion = []
	sumaAptitudesNuevas = 0
	
	siguienteGeneracion = mutarGeneracionCruzada(nuevosCromosomas, pm, n)
	for nuevoCromosoma in siguienteGeneracion:
		aptitudNuevoCromosomaAnalizado = calcularAptitud(nuevoCromosoma, n, matrizA, matrizB)
		aptitudesNuevaGeneracion.append(aptitudNuevoCromosomaAnalizado)
		if aptitudNuevoCromosomaAnalizado < aptitudCromosomasMasApto:
			aptitudCromosomasMasApto = aptitudNuevoCromosomaAnalizado
			cromosomaMasApto = nuevoCromosoma
		sumaAptitudesNuevas = sumaAptitudesNuevas + aptitudNuevoCromosomaAnalizado
	print sumaAptitudes
	print sumaAptitudesNuevas
	if sumaAptitudesNuevas < sumaAptitudes:
		print "Mejoro con respecto la generacion anterior"
	else:
		print "No mejoro con respecto a la generacion anterior"

	# ********************************************************************

principal()
