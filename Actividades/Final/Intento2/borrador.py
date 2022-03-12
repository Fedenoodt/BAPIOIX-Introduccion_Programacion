from os import system
import datetime

path = 'C:/Users/feden/Documents/BAPIOIX/BAPIOIX-Introduccion_Programacion/Actividades/Final/Intento2/'
ventasFile = 'ventas.csv'
ventasCSV = path + ventasFile


def fallo():
    print('\nSe ingresó mal uno de los datos. Intente nuevamente.\n')

def falloINT():
    print('\nIngrese solo números enteros, por favor.\n')

def falloFLOAT_INT():
    print('\nIngrese solo números enteros, o decimales, por favor.')
    
def falloFILE():
    print('\nNo se creó, o no exste el archivo.\nO la ruta no esta especificada.\n')

def procesarVentas():
    existe = True
    lista = 'escribirVentas()'
    try:
        open(ventasCSV,"x")
        existe = False
    except:
        if existe == False:
            #Se pone el sector numerico del código a 1
        else:
            #Se busca el último valor de cada uno de los códigos
            



print(procesarVentas())