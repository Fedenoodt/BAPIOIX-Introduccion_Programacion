import sys
print(list(sys.argv))

ventas = open("/home/fedenoodt/Documentos/BHSIAI/Protocolo 6/GitHub/BAPIOIX/anio1/Primer_Cuatrimestre/BAPIOIX-Introduccion_Programacion/Actividades/Final/ventas.csv", "a")

titulos = ['fecha', 'cantidad', 'código artículo', 'código cliente', 'total venta']

provisional = str(titulos)
titulosSTR = ''

ID_C = 0
ID_L = 0
ID_I = 0

def crearID(tipo, ID_C, ID_I, ID_L):
    if tipo == 'C':
        ID_C += 1
    elif tipo == 'L':
        ID_L += 1
    elif tipo == 'I':
        ID_I += 1

for t in provisional:
    if t != '[' and t != ']' and t != "'" and t != ',':
        print(t, end= '')
        titulosSTR += t

    elif t == ',':
        t = ';'
        print(t, end= '')
        titulosSTR += t
ventas.writelines(titulosSTR)

crearID('C', ID_C, ID_I, ID_L)
crearID('L', ID_C, ID_I, ID_L)

print(ID_C, ID_I, ID_L)