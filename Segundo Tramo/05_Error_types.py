# ERROR TYPES del sistema #

""" ! SyntaxError ! """
# Hemos cometido algun error en la propia sintaxis del codigo, como olvidar los parentesis para la funcion print:

#print "Hola comunidad!" #>>> Descomentar para error
print("Hola comunidad!")

""" ! NameError ! """
# Se da usualmente cuando llamamos a una variable que no está definida aún:

language = "Spanish" #>>> Descomentar para error
print(language)

""" ! IndexError ! """
# Cuando accedemos a un indice que no existe o está fuerea de rango:

my_list = ["Python", 35, 1.65, "Fabrina", "Rovaretti" ]

print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[10]) #>>> Descomentar para error

""" ! ModuleNotFoundError ! """
# Queremos acceder a un modulo que no existe:

#import maths  #>>> Descomentar para error
import math

""" ! AttributeError ! """
# Queremos acceder a una propiedad dentro de un objeto que no existe:

#print(math.PI) #>>> Descomentar para error
print(math.pi)

""" ! KeyError ! """
# Queremos acceder a una llave/clave dentro de un dict y no existe:

my_dict = {"Nombre":"Fabrina", "Apellido":"Rovaretti", "Edad":35, 1:"Golang", 2:"Python"}

#print(my_dict["Apelido"]) #>>> Descomentar para error
print(my_dict["Apellido"])

""" ! TypeError ! """
# Estamos utilizando un tipo de dato que no es valido para ejecutar algo:

my_list = ["Python", 35, 1.65, "Fabrina", "Rovaretti" ]

#print(my_list["0"])  #>>> Descomentar para error
print(my_list[0])

""" ! ImportError ! """
# Estamos importando desde un modulo algo que no existe:

#from math import PI #>>> Descomentar para error
from math import pi as PI

print(PI)

""" ! ValueError ! """
# Estamos intentando realizar conversiones de la forma incorrecta, ya que el valor q le pasamos no es el q necesita:

#my_int_from_str = int("10 años")  #>>> Descomentar para error
my_int_from_str = int("10") 

print(type(my_int_from_str))

""" ! ZeroDivisionError ! """
# Estamos dividiendo x zero y eso no es posible

#print(4/0) #>>> Descomentar para error
print(4/2)