# Modules

"""
Una libreria o fichero externo donde haya código.
Si tenemos código en algún lado externo a nuestro fichero/proyecto podemos hacer uso de él
sin tener que reescribir mil lineas de código.
Esto lo hace escalable y seguro.
Con la palabra reservada: IMPORT
OJO CON LA NOMENCLATURA: no se puede llamar a ficheros que esten encabezados con números.
"""

# llamar a un fichero completo, a todo lo que hay allí
import my_module
# accedemos a una funcion en concreto de ese fichero
my_module.sumValues(5, 3, 1)
my_module.printValues("Hola Python!")


#podemos importar solamente algunas funciones en concreto con FROM:
from my_module import sumValues, printValues

sumValues(3,5,6)
printValues("Hola Python!")

#Tambien tenemos modulos intrinsecos que estan en el core del sistema
import math

print(math.pi) #a traves de un modulo podemos importar VALORES
print(math.pow(2, 8)) #tambien podemos usar funciones especializadas(ej.POTENCIA)

from math import pi as PI_VALUE #Podemos importar 1 funcion del modulo y ponerle un ALIAS con AS a mi eleccion
print(PI_VALUE)