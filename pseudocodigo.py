# -*- coding: utf-8 -*-
import re
import os
from os import listdir
"""
Nombre: division(Var1,Var2,variables)
Parámetros:
	Var1: variable o número entero
	Var2: variable o número entero
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Realiza la division matemática de dos magnitudes, pudiendo ser variables o números 
"""
def division(Var1,Var2,variables):
	resultado=0
	if re.search(r"^[0-9]+$",Var1): #Var1 es un numero
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = int(Var1)/int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = int(Var1)/variables[Var2]
			return resultado
	if re.search(r"^[a-zA-Z]+$",Var1): #Var1 es una variable
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = variables[Var1]/int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = variables[Var1]/variables[Var2]
			return resultado
	return resultado
"""
Nombre: multiplicacion(Var1,Var2,variables)
Parámetros:
	Var1: variable o número entero
	Var2: variable o número entero
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Realiza la multiplicación matemática de dos magnitudes, pudiendo ser variables o números 
"""
def multiplicacion(Var1,Var2,variables):
	resultado=0
	if re.search(r"^[0-9]+$",Var1): #Var1 es un numero
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = int(Var1)*int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = int(Var1)*variables[Var2]
			return resultado
	if re.search(r"^[a-zA-Z]+$",Var1): #Var1 es una variable
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = variables[Var1]*int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = variables[Var1]*variables[Var2]
			return resultado
	return resultado
"""
Nombre: suma(Var1,Var2,variables)
Parámetros:
	Var1: variable o número entero
	Var2: variable o número entero
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Realiza la suma matemática de dos magnitudes, pudiendo ser variables o números 
"""
def suma(Var1,Var2,variables):
	resultado=0
	if re.search(r"^[0-9]+$",Var1): #Var1 es un numero
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = int(Var1)+int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = int(Var1)+variables[Var2]
			return resultado
	if re.search(r"^[a-zA-Z]+$",Var1): #Var1 es una variable
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = variables[Var1]+int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = variables[Var1]+variables[Var2]
			return resultado
	return resultado	
"""
Nombre: resta(Var1,Var2,variables)
Parámetros:
	Var1: variable o número entero
	Var2: variable o número entero
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Realiza la resta matemática de dos magnitudes, pudiendo ser variables o números 
"""
def resta(Var1,Var2,variables):
	resultado=0
	if re.search(r"^[0-9]+$",Var1): #Var1 es un numero
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = int(Var1)-int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = int(Var1)-variables[Var2]
			return resultado
	if re.search(r"^[a-zA-Z]+$",Var1): #Var1 es una variable
		if re.search(r"^[0-9]+$",Var2): #Var2 es un numero
			resultado = variables[Var1]-int(Var2)
			return resultado
		if re.search(r"^[a-zA-Z]+$",Var2): #Var2 es una variable
			resultado = variables[Var1]-variables[Var2]
			return resultado
	return resultado	
"""
Nombre: asignar_resultado(VARi,NUMEROi,variables)
Parámetros:
	VARi: variable
	NUMEROi: número entero
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Asigna NUMEROi a VARi guardando este registro en el diccionario variables 
"""
def asignar_resultado(VARi,NUMEROi,variables):
	variables[VARi]=NUMEROi
	return variables
"""
Nombre: asignar_valor(VARi,NUMEROi,variables)
Parámetros:
	VARi: variable
	NUMEROi: número entero con casting
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Asigna NUMEROi casteado a VARi guardando este registro en el diccionario variables 
"""
def asignar_valor(VARi,NUMEROi,variables):
	variables[VARi]=int(NUMEROi)
	return variables
"""
Nombre: asignar_variable(VARi,VARj,variables)
Parámetros:
	VARi: variable
	VARj: variable
	variables: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	Asigna VARj a VARi guardando este registro en el diccionario variables 
"""
def asignar_variable(VARi,VARj,variables):
	variables[VARi]=variables[VARj]
	return variables
"""
Nombre: PROCESAR_LINEA_NORMAL(LINEA,VARIABLES)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
	VARIABLES: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	realiza las operaciones de scripting que no sean WHILE ni IF
"""
def PROCESAR_LINEA_NORMAL(LINEA,VARIABLES):
# VARIABLE es VARIABLE2 o NUMERO	
	if re.search(r"^[a-zA-Z]+\ses\s[a-zA-Z0-9]+",LINEA): 
#VARIABLE es NUMERO
		if re.search(r"^[a-zA-Z]+\ses\s[0-9]+$",LINEA):			    #linea= "VARi es NUMEROi"
			LINEA=re.sub("\s+","|", LINEA)						    #linea= "VARi|es|NUMEROi"
			LIST= LINEA.split("|") 							        #lista= [VARi,es,NUMEROi]
			VARIABLES=asignar_valor(LIST[0],LIST[2],VARIABLES)      #variables= {(VARi: NUMEROi),...}	
#VARIABLES es OTRA VARIABLE
		if re.search(r"^[a-zA-Z]+\ses\s[a-zA-Z]+$",LINEA): 		    #linea= "VARi es VARj"
			LINEA=re.sub("\s+","|", LINEA)						    #linea= "VARi|es|VARj"
			LIST= LINEA.split("|") 							        #lista= [VARi,es,VARj]
			VARIABLES= asignar_variable(LIST[0],LIST[2],VARIABLES)  #variables= {(VARi: VALOR(VARj)),...}				
#VARIABLE es RESULTADO OPERACION DIVISION 
		if re.search(r"^[a-zA-Z]+\ses\s[a-zA-Z0-9]+\sdividido\s[a-zA-Z0-9]+$",LINEA):
			LINEA=re.sub("\s+","|", LINEA)							#linea= "VARi es STR1 dividido STR2"
			LIST= LINEA.split("|")
			VARIABLES= asignar_resultado(LIST[0],division(LIST[2],LIST[4],VARIABLES),VARIABLES)
#VARIABLE es RESULTADO OPERACION MULTIPLICACION
		if re.search(r"^[a-zA-Z]+\ses\s[a-zA-Z0-9]+\spor\s[a-zA-Z0-9]",LINEA):
			LINEA=re.sub("\s+","|", LINEA)							#linea= "VARi es STR1 por STR2"
			LIST= LINEA.split("|")			
			VARIABLES= asignar_resultado(LIST[0],multiplicacion(LIST[2],LIST[4],VARIABLES),VARIABLES)
#VARIABLE es RESULTADO OPERACION RESTA
		if re.search(r"^[a-zA-Z]+\ses\s[a-zA-Z0-9]+\smenos\s[a-zA-Z0-9]",LINEA):
			LINEA=re.sub("\s+","|", LINEA)							#linea= "VARi es STR1 menos STR2"
			LIST= LINEA.split("|")
			VARIABLES= asignar_resultado(LIST[0],resta(LIST[2],LIST[4],VARIABLES),VARIABLES)
#VARIABLE es RESULTADO OPERACION SUMA	
		if re.search(r"^[a-zA-Z]+\ses\s[a-zA-Z0-9]+\smas\s[a-zA-Z0-9]",LINEA):#linea= "VARi es STR1 mas STR2"
			LINEA=re.sub("\s+","|", LINEA)							#linea= "VARi|es|STR1|mas|STR2"
			LIST= LINEA.split("|")									#lista= [VARi, es, STR1, mas, STR2]
			VARIABLES= asignar_resultado(LIST[0],suma(LIST[2],LIST[4],VARIABLES),VARIABLES)
#MOSTRAR VARIABLE
	if re.search(r"^mostrar\s[a-zA-Z0-9]+",LINEA):
		LINEA=re.sub("\s+","|", LINEA)
		LIST= LINEA.split("|")	
		print LIST[1]+": " + str(VARIABLES[LIST[1]])
"""
Nombre: LINEA_TO_LISTA(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	retorna una lista que contiene los tokens de una sentencia sin espacios
"""
def LINEA_TO_LISTA(LINEA):
	LINEA=re.sub("\s","|", LINEA)	
	LIST= LINEA.split("|")
	return LIST
"""
Nombre: CUMPLO_CONDICION(LINEA,VARIABLES)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
	VARIABLES: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	comprueba la condicion de entrada en un IF o WHILE, retorna un booleano.
"""
def CUMPLO_CONDICION(LINEA,VARIABLES):
	BOOL=False
	LINEA=re.sub("mientras\s","", LINEA)
	LINEA=re.sub("si\s","", LINEA)
	LINEA=re.sub("hacer","", LINEA)
	LINEA=re.sub("entonces","", LINEA)	
	if re.search(r"[a-zA-Z]+\ses\smenor\sque\s[a-zA-Z]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] < VARIABLES[LIST[4]]):
			BOOL=True	
	elif re.search(r"[a-zA-Z]+\ses\smenor\so\sigual\sque\s[a-zA-Z]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] <= VARIABLES[LIST[6]]):
			BOOL=True
	elif re.search(r"[a-zA-Z]+\ses\smayor\sque\s[a-zA-Z]+",LINEA):	
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] > VARIABLES[LIST[4]]):
			BOOL=True
	elif re.search(r"[a-zA-Z]+\ses\smayor\so\sigual\sque\s[a-zA-Z]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] >= VARIABLES[LIST[6]]):
			BOOL=True
	elif re.search(r"[a-zA-Z]+\ses\sigual\sque\s[a-zA-Z]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] == VARIABLES[LIST[4]]):
			BOOL=True	
	elif re.search(r"[a-zA-Z]+\ses\smenor\sque\s[0-9]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] < int(LIST[4])):
			BOOL=True	
	elif re.search(r"[a-zA-Z]+\ses\smenor\so\sigual\sque\s[0-9]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] <= int(LIST[6])):
			BOOL=True
	elif re.search(r"[a-zA-Z]+\ses\smayor\sque\s[0-9]+",LINEA):	
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] > int(LIST[4])):
			BOOL=True
	elif re.search(r"[a-zA-Z]+\ses\smayor\so\sigual\sque\s[0-9]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] >= int(LIST[6])):
			BOOL=True
	elif re.search(r"[a-zA-Z]+\ses\sigual\sque\s[0-9]+",LINEA):
		LIST=LINEA_TO_LISTA(LINEA)
		if (VARIABLES[LIST[0]] == int(LIST[4])):
			BOOL=True
	return BOOL
"""
Nombre: ES_LINEA_NORMAL(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	comprueba si LINEA es diferente a una sentencia IF, WHILE, FIN o SINO, retorna un booleano
"""
def ES_LINEA_NORMAL(LINEA):
	BOOL=True
	if re.search(r"^si.*$",LINEA):
		BOOL=False 
	if re.search(r"^mientras.*$",LINEA):
		BOOL=False
	if re.search(r"^fin.*$",LINEA): 
		BOOL=False	 
	if re.search(r"^sino.*$",LINEA):
		BOOL=False
	return BOOL
"""
Nombre: LEO_WHILE(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	comprueba si LINEA es una sentecia WHILE, retorna un booleano
"""
def LEO_WHILE(LINEA):
	BOOL=False
	if re.search(r"^mientras.*$",LINEA):
		BOOL=True
	return BOOL
"""
Nombre: LEO_END_WHILE(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	comprueba si LINEA es una sentecia final de WHILE (fin mientras), retorna un booleano
"""
def LEO_END_WHILE(LINEA):
	BOOL=False
	if re.search(r"^fin\smientras.*$",LINEA):
		BOOL=True
	return BOOL	
"""
Nombre: LEO_END_WHILE(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	comprueba si LINEA es una sentecia IF, retorna un booleano
"""
def LEO_IF(LINEA):
	BOOL=False
	if re.search(r"^si\s+.*$",LINEA):
		BOOL=True
	return BOOL
"""
Nombre: LEO_END_IF(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	comprueba si LINEA es una sentecia final de IF (fin si), retorna un booleano
"""
def LEO_END_IF(LINEA):
	BOOL=False
	if re.search(r"^fin\ssi.*$",LINEA):
		BOOL=True
	return BOOL
"""
Nombre: LEO_SINO(LINEA)
Parámetros:
	LINEA: linea actual de lectura de un archivo de texto
Utilidad:
	comprueba si LINEA es una sentecia ELSE (sino), retorna un booleano
"""
def LEO_SINO(LINEA):
	BOOL=False
	if re.search(r"^sino*$",LINEA):
		BOOL=True
	return BOOL
"""
Nombre: EJECUTAR_SEGMENTO_CICLO_WHILE(TEXTO, NUM_LINEA, VARIABLES)
Parámetros:
	TEXTO: Archivo de texto en lectura
	NUM_LINEA: valor entero que representa un numero de fila a comprobar en el archivo de texto
	VARIABLES: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	realiza todas las posibles sentencias que pueden pasar dentro de un WHILE
"""
def EJECUTAR_SEGMENTO_CICLO_WHILE(TEXTO, NUM_LINEA, VARIABLES):
	NLINE=0
	for LINEA in TEXTO:
		
		if NLINE<NUM_LINEA:
			NLINE=NLINE+1
			continue
		else:
			if LEO_END_WHILE(LINEA):
				return
			
			if ES_LINEA_NORMAL(LINEA):
				PROCESAR_LINEA_NORMAL(LINEA,VARIABLES)

			if LEO_IF(LINEA):
				EJECUTAR_SEGMENTO_CICLO_IF(TEXTO,NUM_LINEA,VARIABLES)
"""
Nombre: EJECUTAR_SEGMENTO_CICLO_IF(TEXTO,NUM_LINEA,VARIABLES)
Parámetros:
	TEXTO: Archivo de texto en lectura
	NUM_LINEA: valor entero que representa un numero de fila a comprobar en el archivo de texto
	VARIABLES: Diccionario que guarda y actualiza el valor de las variables
Utilidad:
	realiza todas las posibles sentencias que pueden pasar dentro de un IF
"""			
def EJECUTAR_SEGMENTO_CICLO_IF(TEXTO,NUM_LINEA,VARIABLES):
	NLINE=0
	for LINEA in TEXTO:
		
		if NLINE<NUM_LINEA:
			NLINE=NLINE+1
			continue
		else:
			if LEO_END_IF(LINEA):
				return
			
			if LEO_SINO(LINEA):
				return

			if ES_LINEA_NORMAL(LINEA):
				PROCESAR_LINEA_NORMAL(LINEA,VARIABLES)

#INICIO DEL PROGRAMA PRINCIPAL	
ARCHIVO=open("pseudocodigo.txt","r")
TEXTO=ARCHIVO.readlines()
NUM_LINEA=0
SINO = False
SALTAR_LINEAS = False
VARIABLES=dict()
for LINEA in TEXTO:

	#############################################################
	if ES_LINEA_NORMAL(LINEA):
		if SALTAR_LINEAS == False:
			PROCESAR_LINEA_NORMAL(LINEA,VARIABLES)
    #############################################################
	if LEO_IF(LINEA) or SINO == True:
		if CUMPLO_CONDICION(LINEA,VARIABLES) and SINO == False:
			EJECUTAR_SEGMENTO_CICLO_IF(TEXTO,NUM_LINEA,VARIABLES)
			SALTAR_LINEAS = True
		else:
			SALTAR_LINEAS = True
			SINO = True
			if LEO_SINO(LINEA):
				SALTAR_LINEAS = False

	if LEO_END_IF(LINEA):
		SINO = False
		SALTAR_LINEAS = False
	############################################################
	if LEO_WHILE(LINEA):
		if CUMPLO_CONDICION(LINEA,VARIABLES):
			while CUMPLO_CONDICION(LINEA,VARIABLES):
				EJECUTAR_SEGMENTO_CICLO_WHILE(TEXTO,NUM_LINEA,VARIABLES)
			SALTAR_LINEAS = True
		else:
			SALTAR_LINEAS = True

	if LEO_END_WHILE(LINEA):
		SALTAR_LINEAS = False
	############################################################
	NUM_LINEA=NUM_LINEA+1

ARCHIVO.close()	
