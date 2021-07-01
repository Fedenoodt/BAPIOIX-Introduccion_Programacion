#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #~~~~~~~~~~~~~//\\~~~~~~~~~~~~~#
        #####RESOLVER######ACA##########
pasar = False
abecedario = 'abcdefghijklmnñopqrstuvwxyz'
numeros = '0123456789'

def main(frase, abecedario, numeros):
    caracterNumerico = caracteresNumericos(frase, abecedario, numeros)
    caracter = caracteres(frase, abecedario, numeros)
    cesarCaracteres(frase, abecedario, desplazamiento, caracter, numeros)
    print(caracterNumerico, caracter)
    
def desplazamiento(direccion, desplazamiento):
    if direccion == 'I':
        desplazamiento = 0 - desplazamiento
    return desplazamiento
    #####RESOLVER######ACA##########
    #Falla el ingreso de desplazamiento, que si o si hay que hacerlo por funciones separadas, porque no se escribe en el transcurso de indice.
    
def indice(direccion, desplazamiento):
    if direccion == 'D':
        main(frase, abecedario, numeros)
    elif direccion == 'I':
        desplazamiento = 0 - desplazamiento
        main(frase, abecedario, numeros)
    return desplazamiento

def caracteresNumericos(frase, abecedario, numeros):
    caracterNumerico = False
    for f in range(0, len(frase)):
        for n in range(0, len(numeros)):
            if frase[f] == numeros[n]:
                caracterNumerico = True
    return caracterNumerico
            
def caracteres(frase, abecedario, numeros):
    caracter = False
    for f in range(0, len(frase)):
        for a in range(0, len(abecedario)):
            if frase[f] == abecedario[a]:
                caracter = True
    return caracter
            
def cesarCaracteres(frase, abecedario, desplazamiento, caracter, numeros):
    if caracter:
        ciclosABC = []
        for i in range(0, 3):
            for a in range(0, len(abecedario)):
                ciclosABC.append(abecedario[a])
        print(ciclosABC[27], ciclosABC[53])
        for c in range((27 + (desplazamiento)), (54 + (desplazamiento))):
            print(ciclosABC[c])
        for f in range(0, len(frase)):
            print(frase[f])
        
                
def fallo():
    print('Ingresó mal alguno de los datos. Intentelo de nuevo.')
   
while not pasar:
    try:
        direccion = input('¿Dirección del codificado? ("D" para la derecha, "I" para la izquierda).\n ').upper()
        desplazamiento = int(input('Ingrese número de letras a desplazar:\n '))
        frase = input('Ingrese una frase:\n ')
        if direccion == 'D' or direccion == 'I':
            pasar = True
        else:
            fallo()

    except:
        fallo()

desplazamiento = desplazamiento(direccion, desplazamiento)
indice(direccion, desplazamiento)