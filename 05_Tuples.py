# TUPLAS : Conjunto de elementos inmutables. Al crearlas inicializamos valores cerrados.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.68, "Fabrina", "Rovaretti")
# Clase de dato 'class tuple'
print(type(my_tuple)) 

#Podemos consultar los index
print(my_tuple[0])
print(my_tuple[-1])

#Podemos sumar tuplas y armar una nueva tupla mas grande.
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple[2:4])

# Si quisiera modificar los datos de una tupla, podemos convertirla en LISTA
my_tuple = list(my_tuple)
print(type(my_tuple))

# ...modificamos 
my_tuple.insert(4, "Azul")
print(my_tuple)
# ...y luego la volvemos a convertir en TUPLA
my_tuple = tuple(my_tuple)
print(type(my_tuple))

# Llamativamente se puede BORRAR
del my_tuple
print(my_tuple)


