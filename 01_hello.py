#esto es un comentario: hola mundo
# nuestro hola en python
print("Hola Ipython!")
print('Hola Ipython!')


# Consultar el tipo de dato
print(type("Este es un string"))
print(type(5))
print(type(10.5))
print(type(True))
print(type(3 + 1J))


my_string_example = "Este es un string"
my_int_example = 5
my_float_example = 10.5
my_bool_example = True

# Concatenacion de Argumentos en las funciones
print(my_string_example, my_int_example, my_float_example, my_bool_example)

#Conversión de tipo en variables con func 'str()
my_int_to_str_variable = str(my_int_example)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
print("Este es el valor de:", my_bool_example)

# Algunas funciones del sistema:
print(len(my_string_example)) #da la longitud de caracteres de la cadena de texto

# Multiples variables en una sola linea:
name, surname, alias, age = "Fabrina", "Rovaretti", "FLAKIRA", 35
print("Mi nombre es:", name, surname, ". Tengo", age, "años,", "y mi alias es:", alias)

# Tipos de Comentarios
# Trabajar con input del usuario
"""
name = input('Como es tu nombre?: ')
age = input('..y cuantos años tenes?: ')

print(name)
print(age)
"""

# No es posible Forzar tipo de variable, se puede seguir cambiando de tipo
address: str = "27 de abril 370"
address = 370
print(address)
print(type(address))

print(type(print("Que tipo tiene la funcion print?"))) #Tipo de dato 'NoneType'
