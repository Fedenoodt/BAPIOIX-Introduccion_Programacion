from os import system
import datetime

path = 'C:/Users/feden/Documents/BAPIOIX/BAPIOIX-Introduccion_Programacion/Actividades/Final/Intento2/'
ventasFile = 'ventas.csv'
ventasCSV = path + ventasFile

def zona():
    prov = input('Ingrese la provincia del comprador. → ')
    largoNombre = len(prov)
    provincia = prov[0] + prov[(largoNombre - 1)//2] + prov[largoNombre - 1]
    bien = False
    brujula = ['N', 'E', 'O', 'S']
    while bien == False:
        news = input('Ingrese número si es zona... \n1) Norte\n2) Este\n3) Oeste\n4) Sur.\n → ')
        if news != 1 or news != 2 or news != 3 or news != 4:
            bien == False
        else:
            zona = provincia + brujula[news - 1]
    return zona

def leerVentas():
    ventas=open(ventasCSV,"r")
    print(ventas.read())
    ventas.close()
    print('Esas son todas las ventas.\nPresione enter para continuar')
    input()

vendedoresFile = 'vendedores.csv'
vendedoresCSV = path + vendedoresFile

def leerVendedores():
    vendedores=open(vendedoresCSV,"r")
    print(vendedores.read())
    vendedores.close()
    print('Esas son todas las ventas.\nPresione enter para continuar')
    input()

def escribirVentas():
    venta = []

#___________________________________________________#
    fecha = ''
    dia = str(datetime.date.today())
    for f in dia:
        if f != '-':
                fecha = fecha + f
    venta.append(fecha)
#___________________________________________________#
    cantidad = ''
    bien = False
    while bien == False:
        try:
            cantidad = int(input('Ingrese el número de unidades el producto.\n→ '))
            venta.append(cantidad)
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
            if articulo != 1 or articulo != 2 or articulo != 3 or articulo != 4:
                bien = False
            else:
                bien = True
                articulo = tipoArticulos[articulo - 1]
                venta.append(articulo)
        except:
            falloINT()
#___________________________________________________#
    provincia = zona()
    venta.append(provincia)
#___________________________________________________#
#escribirVentas()


def escribirVendedores():
    vendedor = []

    provincia = zona()
    vendedor.append(provincia)
#___________________________________________________#
    nombre = input('Ingrese nombre del vendedor → ')
#___________________________________________________#

def fallo():
    print('\nSe ingresó mal uno de los datos. Intente nuevamente.\n')

def falloINT():
    print('\nIngrese solo números enteros, por favor.\n')
    
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
        except:
            ventas=open(ventasCSV,"r")
            leerVentas()
            ventas.close

    if opcion == 2:
        try:
            ventas=open(ventasCSV,"x")
            escribirVentas()
            ventas.close
        except:
            ventas=open(ventasCSV,"w")
            escribirVentas()
            ventas.close
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