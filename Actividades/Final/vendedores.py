"""
path='/home/eduardo/Python/'
ventas=open("ventas.csv","r")
texto = ventas.read()
print (texto)
ventas.close()
texto="20210704; 200; C007; SfeNE0007; 800"
ventas=open("ventas.csv","a")
ventas.writelines(texto)
ventas.close()
"""
from os import system
import datetime

path = 'C:/Users/Federico/Downloads/'
ventasCSV = path + 'ventas.csv'

def leerVentas():
    ventas=open(ventasCSV,"r")
    print(ventas.read())
    ventas.close()
    print('Presione enter para continuar')
    input()

def fallo():
    print('\nSe ingresó mal uno de los datos. Intente nuevamente.\n')

def falloINT():
    print('\nIngrese solo números enteros, por favor.\n')
    
def falloFILE():
    print('\nNo se creó, o no exste el archivo.\nO la ruta no esta especificada.\n')




articulo_cID = 0
articulo_lID = 0
articulo_iID = 0
articulo_3DID = 0
cliente_ID = 0

def registros(archivo, ventasCSV, lista):
    texto = str(lista)
    letras = ''

    for l in texto:
        if l != '[' and l != ']' and l != "'" and l != ',':
            print(l, end= '')
            letras += l

        elif l == ',':
            l = ';'
            print(l, end= '')
            letras += l
    print(letras)
    archivo = open(ventasCSV,"a")
    archivo.writelines(letras + '\n')
    archivo.close()

def registroFecha():
    
    dia = str(datetime.date.today())

    fechaRegistro = ''
    for d in dia:
        if d != '-':
            fechaRegistro += d

    return fechaRegistro

def registroCantidad():

    pase = False
    while not pase:
        try:
            cantidad = int(input('Ingrese la cantidad: '))
            pase = True
        except ValueError:
            falloINT()
        except:
            fallo()
    return cantidad

def categorizarArticulo():
    articulo = 0

    pase = False
    while not pase:
        try:
            categoria = int(input('Ingrese número, según la categoría \nque corresponda al ártículo:\n1- Cocina\n2- Librería\n3- Industria\n4- Impresión 3D\n'))

            pase = True
            
        except ValueError:
            falloINT()
        except:
            fallo()
    return categoria

def registroZona(cliente_ID):
    try:
        zona = input('Ingrese la zona de venta:\n')
        zona = zona[0] + zona[-2] + zona[-1]

        news = int(input('Según número, ingrese que\nsector de la zona es:\n1- Norte  2- Noreste  3- Noroeste  4- Este\n5- Oeste  6- Sudeste  7- Sudoeste  8- Sur\n'))

        brujula = ['N', 'NE', 'NO', 'E', 'O', 'SE', 'SO', 'S']
        posicion = brujula[news - 1]

        cliente_ID += 1

        ceros = 4 - len(str(cliente_ID))
        ID = (ceros * '0') + str(cliente_ID)


    except:
        fallo()

    return zona + posicion + ID


def registroArticulo(articulo_cID, articulo_lID, articulo_iID, articulo_3DID):
    tipoArticulo = categorizarArticulo()
    articulo = ''

    if tipoArticulo == 1:
        articulo_cID += 1
        articulo = 'C' + ((3 - len(str(articulo_cID))) * '0') + str(articulo_cID)
    elif tipoArticulo == 2:
        articulo_lID += 1
        articulo = 'L' + ((3 - len(str(articulo_lID))) * '0') + str(articulo_lID)
    elif tipoArticulo == 3:
        articulo_iID += 1
        articulo = 'I' + ((3 - len(str(articulo_iID))) * '0') + str(articulo_iID)
    elif tipoArticulo == 4:
        articulo_3DID += 1
        articulo = 'I' + ((3 - len(str(articulo_3DID))) * '0') + str(articulo_3DID)    

    return(articulo, articulo_cID, articulo_lID, articulo_iID, articulo_3DID)

def registrarVentas(identificacion):
    venta = [registroFecha(), registroCantidad(), identificacion, registroZona(cliente_ID)]
    print(venta)
    registros("ventas.csv", ventasCSV, venta)
    
def registrarNombre(valor):
    try:
        valor = input("Ingrese el apellido, a continuación, el nombre del vendedor.\n\n")
    except:
        fallo()
    return valor

def registrarValor(numero):
    numero = 0    
    while numero < 0 and numero > 100:
        try:
            numero = int(input("Ingrese porcentaje de la comisión, y después, el monto mínimo.\n\n"))
            
        except ValueError:
            falloINT()
        except:
            fallo()

open(ventasCSV,"a")

opcion=1
while opcion !=0:
    print('======================================================')
    print('Ingrese la opción deseada ó "0" para salir: ')
    print('------------------------------------------------------')
    print('1.- Ver el archivo de ventas.')
    print('2.- Registrar una venta')
    print('======================================================')
    try:
        opcion=int(input('>>>> '))
        if opcion != 0 and opcion == 1 or opcion == 2:
            if opcion == 1:
                leerVentas()
            if opcion == 2:
                articulos = registroArticulo(articulo_cID, articulo_lID, articulo_iID, articulo_3DID)
                articulo = articulos[0]

                if articulo_cID < articulos[1]:
                    articulo_cID += articulos[1]
                    identificacion = articulo

                elif articulo_iID < articulos[2]:
                    articulo_iID += articulos[2]
                    identificacion = articulo

                elif articulo_lID < articulos[3]:
                    articulo_lID += articulos[3]
                    identificacion = articulo

                elif articulo_3DID < articulos[4]:
                    articulo_3DID += articulos[4]
                    identificacion = articulo
                
                registrarVentas(identificacion)
                
    except ValueError:
        falloINT()
    except FileNotFoundError:
        falloFILE()
    except:
        fallo()
