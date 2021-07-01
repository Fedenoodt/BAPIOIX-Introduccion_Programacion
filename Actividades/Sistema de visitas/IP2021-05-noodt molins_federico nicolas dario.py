        #~~~~~~~~~~~~~//Definiciones\\~~~~~~~~~~~~~#

# -*- coding: utf-8 -*-
import datetime

entradas = ('nombre', 'destino', 'contacto')
datos = {'nombre' : '', 'destino' : '', 'contacto' : '', 'ingresa' : '', 'egresa' : ''}
tiempo = str(datetime.datetime.now())

visitas = {}

        #~~~~~~~~~~~~~//Funciones\\~~~~~~~~~~~~~#

def ingreso(entradas, datos, tiempo, diccionario):
    print('Ingrese los siguientes datos.')
    for i in range(len(entradas)):
        print(entradas[i].capitalize())
        datos[entradas[i]] = input('>   ')
        
    print('Ingrese su DNI, sin comas ni puntos.')
    dni = int(input('>   '))
    datos['ingresa'] = tiempo
    print(dni, datos)
    visitas[dni] = datos
    print(visitas)
    
    return diccionario, dni

        #~~~~~~~~~~~~~//Cuerpo\\~~~~~~~~~~~~~#

for i in range(2):
    variables = ingreso(entradas, datos, tiempo, visitas)
    visitas = variables[0]
    dni = variables[1]


    
print(visitas)

        #####RESOLVER######ACA##########
        # Bien, faltaría diseñar algún sistema que tome lo ingresado por el
        # usuario, el dni y los datos, y genere un bucle de n visitantes.
