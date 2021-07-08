inmuebles = open("/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/BAPIOIX/anio1/Primer_Cuatrimestre/BAPIOIX-Introduccion_Programacion/Actividades/Ejercicio_inmuebles/inmuebles.csv", "r")

        #=# 1 #=# #~~~~~~~~~~~~~//Lista de Vendedores\\~~~~~~~~~~~~~#

        #~~~~~~~~~~~~~//Definiciones\\~~~~~~~~~~~~~#

listado = {}
titulos = []
data = []

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
referencia = []
fecha_alta = []
tipo = []
operacion = []
provincia = []
superficie = []
precio_venta = []
fecha_venta = []
vendedor = []

        #~~~~~~~~~~~~~//Funciones\\~~~~~~~~~~~~~#

def operacionador(linea, valor, almacenaje):
    for l in linea:
        if l == ';' or l == '\n' or l == '"' or l == '':
            if valor != '':    
                almacenaje.append(valor)
            valor = ''
        else:
            valor += l

def primeraLinea(titulos):
    titulo = ''
    lineaUno = inmuebles.readline()
    operacionador(lineaUno, titulo, titulos)
    
def crearDiccionario():
    primeraLinea(titulos)
    for t in range(len(titulos)):
        listado[titulos[t]] = []
    return listado

def informacion(data):
    detalle = ''
    for linea in inmuebles:
        operacionador(linea, detalle, data)
        
    return data

def versionador(data, lista, posicion):
    for d in range(0, len(data)):
        if data[d] != '':
            lista.append(data[posicion])

        #####RESOLVER######ACA##########
        # Hace falta completar esta funcion, que va a insertar en cada lista, la informacion.

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main(data):
    listado = crearDiccionario()
    linea = inmuebles.readline()
    data = informacion(data)
            

    print(listado)
            
        #~~~~~~~~~~~~~//Cuerpo\\~~~~~~~~~~~~~#


# main(data)

a = informacion(data)
print(a)
        #####RESOLVER######ACA##########
