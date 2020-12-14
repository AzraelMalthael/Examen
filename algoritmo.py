# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:43:52 2020

for i in range(0,len(datos)):
        aux1=datos[i]
        aux2=datos[i+1]
        
        for i in range(0,len(datoso)):
    datoso[i]=datoso[i]**3+datoso[i]**2+datoso[i]

for i in datoso:
    numbin.append('{:012d}'.format(int(binarizar(i))))

@author: Windows Vista
"""
import numpy as np

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

def cruce(numero_cad,datos,i):
    aux1=""
    aux2=""
    aux1=datos[i]
    aux2=datos[i+1]
    subcad1=aux1[len(aux1)-numero_cad:]
    subcad2=aux2[len(aux2)-numero_cad:]
    datos[i]=aux1[:len(aux1)-numero_cad]+subcad2
    datos[i+1]=aux2[:len(aux2)-numero_cad]+subcad1
    
def muta(numero,datos,i):
    aux1=""
    aux1=datos[i]
    subcad1=aux1[:len(aux1)-numero]
    subcad2=aux1[len(aux1)-numero+1:]
    subcad3=aux1[len(aux1)-numero:len(aux1)-numero+1]
    datos[i]=aux1.replace(subcad1,subcad2)
    if subcad3=='1':
        subcad3='0'
    else: 
        subcad3='1'
    datos[i]=subcad1+subcad3+subcad2
    
datos=[1,2,4,5,3,8,9,6]
numbin=[]
for i in range(0,3):   
    datoso=sorted(datos)
    for j in range(0,len(datoso)):
        datoso[j]=(datoso[j]**3)+datoso[j]**2+datoso[j]
    for j in datoso:
        numbin.append('{:020d}'.format(int(binarizar(j))))
    cant=int(len(numbin)/2)
    for j in range(0,cant):
        cruce(2,numbin,j*2)
    for j in range(len(numbin)):
        muta(2,numbin,j)
    datoso=[] 
    datos=[]
    for j in numbin:
        datos.append(binario_a_decimal(j))
    numbin=[]
print(datoso)



