from os import system
import datetime

ventasExiste = False
path = 'C:/Users/feden/Documents/BAPIOIX/BAPIOIX-Introduccion_Programacion/Actividades/Final/Intento2/'
ventasFile = 'ventas.csv'
ventasCSV = path + ventasFile

def zona():
    prov = input('Ingrese la provincia. → ').upper()
    largoNombre = len(prov)
    provincia = prov[0] + prov[(largoNombre - 1)//2] + prov[largoNombre - 1]
    bien = False
    brujula = ['N', 'E', 'O', 'S']
    print('Ingrese número si es zona... \n1) Norte\n2) Este\n3) Oeste\n4) Sur.')
    while bien == False:
        try:
            news = int(input('→ '))
            if news == 1 or news == 2 or news == 3 or news == 4:
                bien = True
                zona = provincia + brujula[news - 1]
        except:
            falloINT()
    return zona

def leerVentas():
    ventas=open(ventasCSV,"r")
    print(ventas.read())
    ventas.close()
    print('Esas son todas las ventas.\nPresione enter para continuar...')
    input()

vendedoresFile = 'vendedores.csv'
vendedoresCSV = path + vendedoresFile

def leerVendedores():
    vendedores=open(vendedoresCSV,"r")
    print(vendedores.read())
    vendedores.close()
    print('Esas son todas los vendedores.\nPresione enter para continuar...')
    input()

def escribirVentas():
    ventas = []

#___________________________________________________#
    fecha = ''
    dia = str(datetime.date.today())
    for f in dia:
        if f != '-':
                fecha = fecha + f
    ventas.append(fecha)
#___________________________________________________#
    cantidad = ''
    bien = False
    while bien == False:
        try:
            cantidad = int(input('Ingrese el número de unidades el producto.\n→ '))
            ventas.append(cantidad)
            bien = True
        except:
            falloINT()
#___________________________________________________#
    bien = False
    tipoArticulos = ['CO', 'LI', 'IM', 'IN']
    print('''♦ Ingrese 1, si el producto es de cocina.\n♦ Ingrese 2 si es de librería.
    \n♦ Ingrese 3 si es Impresión 3D.\n♦ Ingrese 4 si es de Industria''')
    while bien == False:
        try:
            articulo = int(input('→ '))
            if articulo == 1 or articulo == 2 or articulo == 3 or articulo == 4:
                bien = True
                articulo = tipoArticulos[articulo - 1]
                ventas.append(articulo)
        except:
            falloINT()
#___________________________________________________#
    provincia = zona()
    ventas.append(provincia)
#___________________________________________________#
    return ventas
#escribirVentas()


def escribirVendedores():
    vendedores = []

    provincia = zona()
    vendedores.append(provincia)
#___________________________________________________#
    nombre = input('Ingrese nombre del vendedor. → ')
    vendedores.append(nombre)
#___________________________________________________#
    apellidos = input('Ingrese apellidos del vendedor. → ')
    vendedores.append(apellidos)
#___________________________________________________#
    bien = False
    while bien == False:
        try:
            comiPorcentaje = float(input('Ingrese el porcentaje de la comisión. → '))
            bien = True
            vendedores.append(comiPorcentaje)
        except:
            falloFLOAT_INT()
#___________________________________________________#
    bien = False
    while bien == False:
        try:
            comiTotal = float(input('Ingrese el fijo de la comisión. → '))
            bien = True
            vendedores.append(comiTotal)
        except:
            falloFLOAT_INT()
#___________________________________________________#
    bien = False
    while bien == False:
        try:
            fijoMinimo = float(input('Ingrese el mínimo para cobrar el fijo. → '))
            bien = True
            vendedores.append(fijoMinimo)
        except:
            falloFLOAT_INT()
#___________________________________________________#
    return vendedores

def fallo():
    print('\nSe ingresó mal uno de los datos. Intente nuevamente.\n')

def falloINT():
    print('\nIngrese solo números enteros, por favor.\n')

def falloFLOAT_INT():
    print('\nIngrese solo números enteros, o decimales, por favor.')
    
def falloFILE():
    print('\nNo se creó, o no exste el archivo.\nO la ruta no esta especificada.\n')

opcion = 1

fecha = ''
cantidad = ''
articulo_ID = ''
tipoArticulo = ''
cliente_ID = ''
zonaCliente = ''
total = ''


while opcion != 0:

    if opcion == 1:
        try:
            ventas=open(ventasCSV,"x")
            leerVentas()
            ventas.close
            ventasExiste = True
        except:
            ventas=open(ventasCSV,"r")
            leerVentas()
            ventas.close
            ventasExiste = True

    if opcion == 2:
        try:
            ventas=open(ventasCSV,"x")
            escribirVentas()
            ventas.close
            ventasExiste = True
        except:
            ventas=open(ventasCSV,"w")
            escribirVentas()
            ventas.close
            ventasExiste = True
    if opcion == 3:
        try:
            vendedores=open(vendedoresCSV,"x")
            leerVendedores()
            vendedores.close
        except:
            vendedores=open(vendedoresCSV,"r")
            leerVendedores()
            vendedores.close

    if opcion == 4:
        try:
            vendedores=open(vendedoresCSV,"x")
            escribirVendedores()
            vendedores.close
        except:
            vendedores=open(vendedoresCSV,"w")
            escribirVendedores()
            vendedores.close