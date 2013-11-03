#a_mutar=[['A','B','C','D','E','F'],['D','C','F','E','B','A'],['C','B','E','A','F','D']]
a_mutar=[['A','B','C','D','E','F']]
mutar_c=[]
def mutacionPrim(cromosoma,gen_f):
	if gen_f[0]>gen_f[1]:
		mut1=gen_f[1]
		mut2=gen_f[0]
	else:
		mut1=gen_f[0]
		mut2=gen_f[1]
	cromosoma_mutado=cromosoma
	aux1= cromosoma[mut1-1]
	aux2= cromosoma[mut2-1]
	cromosoma_mutado[mut1-1]=aux2
	cromosoma_mutado[mut2-1]=aux1
	#print cromosoma_mutado
	return cromosoma_mutado

#reacomoda los elementos del cromosoma de acuerdo a la funcion de mutacion
def mutacionSec(elemento,gen_f):
	elem_mutado=elemento
	if gen_f[0]>gen_f[1]:
		mut1=gen_f[1]
		mut2=gen_f[0]
	else:
		mut1=gen_f[0]
		mut2=gen_f[1]
	aux=elemento[mut1-1:mut2]
	aux2=aux[::-1]
	for i in range (0,len(elemento)):
		if (i == mut1):
			for j in range (0, len(aux2)):
				elem_mutado[i-1]=aux2[j]
				i=i+1
	return elem_mutado

#funcion para mutar los cromosomas seleccionados, aplicando el metodo dos de mutacion
#recibe: lista de cromosomas que van a mutar
#devuelve: lista de cromosomas mutados

def mutar(a_mutar):
	cromosomas_mutados=[]
	#genera 2 aleatorios enteros, pasando como parametro el tamano del cromosoma
	#operadores=generadorEnt(w)
	#operadores=[5,2]
	gen_f=[5,2]
	#lee un cromosoma y aplica mutacion en las posiciones definidas
	for i in range(0,len(a_mutar)):
		elemento=a_mutar[i]
		elemento_mutado=mutacionPrim(elemento,gen_f)
		for j in range(0,len(elemento)):
			if(elemento[j]==elemento_mutado[j]):
				b_igual=1
			if(elemento[j]!=elemento_mutado[j]):
				b_igual=0
		if(b_igual==1):
			elemento_mutado=mutacionSec(elemento, gen_f)
		cromosomas_mutados.append(elemento_mutado)
		print elemento_mutado
	return cromosomas_mutados

mutar(a_mutar)
