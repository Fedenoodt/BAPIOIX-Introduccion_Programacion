#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

temperatura = float(input('Ingrese la temperatura:\n '))
unidad = float(input('Ingrese según número, la unidad que esta temperatura es:\n1|Celsius\n2|Fahrenheit\n3|Kelvin\n\n\n '))

#=////==////==////==////==////==////==////==////==////==////==////==////==////==////==////==////=#

def celsius(temperatura, unidad):
    if unidad == 1:
        celsius = temperatura
        fahrenheit = temperatura * 1.8 + 32
        kelvin = temperatura + 273.15
        print('Temperatura Celsius |', celsius, 'º.\n',
              'Temperatura Fahrenheit|', fahrenheit, 'º.\n',
              'Temperatura Kelvin|', kelvin, 'º.\n')
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
def fahrenheit(temperatura, unidad):
    if unidad == 2:
        celsius = (temperatura - 32) / 1.8
        fahrenheit = temperatura
        kelvin = 