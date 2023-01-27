# Loops: ciclos, bucles. 
""" 
Sirven para desatar iteraciones sobre un bloque de código (while), o sobre un conjunto de valores (for).
A un bucle hay que pasarle UNA CONDICIÓN, pero que CAMBIE (si no haremos un bucle infinito)
"""

# While : "mientras sea True haz esto:"

my_condition = 0


while my_condition < 10:
    print(my_condition)
    my_condition += 2
# Opcionalmente se puede enlazar un ELSE cuando culmine el ciclo. 
# Convive con WHILE porque vendria a ser como un IF reiterativo.
else: 
    print("Mi condición es igual o mayor que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es justo 15. Se detiene la ejecución!")
        # Se cumple la condición del While pero podemos ROMPER el bucle cuando se cumple una condición intermedia.
        break
   
    print(my_condition) #ESTO no se va a ejecutar cuando el break rompa el ciclo
    
print("La ejecución sigue continuando")

# FOR
"""
FOR se va a ejecutar tantas veces como elementos tenga almacenados la estructura de datos.
Está atado a un elemento finito de datos contenidos en una LISTA, SET, TUPLA, DICCIONARIO.
"""
print("For sobre LISTS:")
my_list = [35, 35, 62, 38, 45]

for element in my_list:
    print(element)

print("For sobre TUPLES:")
my_tuple = (35, 1.68, "Fabrina", "Rovaretti")
for element in my_tuple:
    print(element)

print("For sobre SETS:")
my_set = {"Georgina", 30, 1.61}
for element in my_set:
    print(element)

print("For sobre DICTIONARIES:")
# Va a iterar sobre las LLAVES del diccionario
my_dict = {
    "Nombre":"Daniel", 
    "Apellido":"Rovaretti",
    "Edad":61,
    "Lenguajes":{"Python","Javascript","html"},
    2023: "Nuevos aprendizajes"
    }

for element in my_dict:
    print(element)
    if element == "Edad":
        break
# ELIF no se puede utilizar con el FOR (a no ser que lo anidemos en un IF).
    #elif element == 1:
    #print("El elemento es igual a 1")
else: 
    print("Se ejecuta")

# para imprimir los VALUES de un DICT:
print("For sobre VALUES del DICTIONARY:")
for element in my_dict.values():
    print(element)
# FOR tambien convive con ELSE
else:
    print("El buble FOR para mi diccionario hafinalizado")

print("Uso del CONTINUE:")
my_list = [35, 35, 62, 38, 45]

for element in my_list:
    print(element)
    if element == 38:
        print("Se cumple la condicion de haber llegado al valor 38 pero continua")
        continue
        print("Se ejecuta?") #no se ejecuta, porque CONTINUE vuelve a comenzar el ciclo 
