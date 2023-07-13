# LIST COMPREHENSION #
# Lista original que vamos a usar como recurso
# para crear nuevas listas o trabajar en base a estos indices
my_original_list_1 = [35, 35, 62, 38, 45]

my_list_1 = [i for i in my_original_list_1]
print(my_list_1)

my_original_list_2 = [0, 1, 2, 3, 4, 5, 6, 7]
print(f"{my_original_list_2}\n#1 Imprime mi lista original y resulta que es un rango")

my_list_2 = [i for i in range(8)]
print(f"{my_list_2}\n#2 Imprime una nueva lista a partir de for a la funcion range")
# Si tuviera que abarcar un rago mas grande (x ej 80) me ahorro esribir la lista a mano

# Otra forma de crear una lista a partir de range
my_range = range(8)
print(f"{list(my_range)}\nConvirtiendo a lista una variable q almacena un rango")

# Creamos una nueva lista operando los elementos de una lista original
my_list_3 = [i + 1 for i in range(8)]
print(f"{my_list_3}\n#3 Opera sumando 1 a cada elemento q itera y lo guarda en una nueva lista")

my_list_4 = [i * i for i in range(8)]
print(f"{my_list_4}\n#4 Opera multiplicando x si mismo cada elemento q itera y lo guarda en una nueva lista")

# Puede complejizase aun más incluyenfo una funcion como operacion
def sum_five(number):
    return number + 5

my_list_5 = [sum_five(i) for i in range(8)]
print(f"{my_list_5}\n#5 Define una funcion personalizada sumadora de 5 a cada elemento q itera y lo guarda en una nueva lista")
