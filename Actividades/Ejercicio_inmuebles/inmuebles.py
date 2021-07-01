inmuebles = open("inmuebles.csv", "r")

        #=# 1 #=# #~~~~~~~~~~~~~//Lista de Vendedores\\~~~~~~~~~~~~~#

        #~~~~~~~~~~~~~//Definiciones\\~~~~~~~~~~~~~#

operacion = {}
titulos = []
detalles = []

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
        operacion[titulos[t]] = ''
    return operacion

def informacion(detalles):
    detalle = ''
    linea = inmuebles.readline()
    operacionador(linea, detalle, detalles)
    return detalles

def insercion(titulos, detalles, operacion):
    for i in range(len(detalles)):
        operacion[titulos[i]] = detalles[i]
    return operacion

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main(detalles):
    operacion = crearDiccionario()
    detalles = informacion(detalles)
            
    operacion = insercion(titulos, detalles, operacion)

    print(operacion)
            
        #~~~~~~~~~~~~~//Cuerpo\\~~~~~~~~~~~~~#


main(detalles)
    
        #####RESOLVER######ACA##########
    #Logramos que se junten los datos, con sus títulos en un
    #diccionario. Ahora nos hace falta que se creen diccionarios
    #en una lista, con las distintas operaciones y los mismos
    #títulos.