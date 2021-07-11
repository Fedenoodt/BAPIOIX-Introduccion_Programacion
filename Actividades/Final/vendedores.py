#import sys
#print(list(sys.argv))


# "reconocimiento()" tiene como misión principal, tomar identificaciones existentes, (si es que existe un archivo)
# actualizarlas, si es asi, y si no, crear nuevas.
def reconocimiento():
    try:
        ventas = open("/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/BAPIOIX/anio1/Primer_Cuatrimestre/BAPIOIX-Introduccion_Programacion/Actividades/Final/ventas.csv", "r")
    except FileNotFoundError:
        ventas = open("/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/BAPIOIX/anio1/Primer_Cuatrimestre/BAPIOIX-Introduccion_Programacion/Actividades/Final/ventas.csv", "a")
    return ventas

ventas = reconocimiento()

titulosLista = ['fecha', 'cantidad', 'código artículo', 'código cliente', 'total venta']

articulo_cID = 0
articulo_lID = 0
articulo_iID = 0
articulo_3DID = 0
cliente_ID = 0

def fallo():
    print('\nSe ingresó mal uno de los datos. Intente nuevamente.\n')
def falloINT():
    print('\nIngrese solo números enteros, por favor.\n')

def registros(lista):
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
    ventas.writelines(letras + '\n')

def registroFecha():
    import datetime
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

    return(articulo)


registros(titulosLista)

venta = [registroFecha(), registroCantidad(), registroArticulo(articulo_cID, articulo_lID, articulo_iID, articulo_3DID),registroZona(cliente_ID)]
print(venta)

registros(venta)

ventas.close()