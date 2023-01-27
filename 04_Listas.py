# LISTAS _ Estructura de datos (como arrays) nos sueledar operaciones mas complejas propias de las listas.
"""
Una caja en donde podemos añadir elementos en posiciones. Los index empiezan desde #0.

"""
# pueden definirse con list() o con [] ambivalentemente.
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 35, 62, 38, 45]
print(len(my_list))

my_other_list = [35, 1.65, "Fabrina", "Rovaretti" ]
print(type(my_other_list)) #El type de la lista es 'class list'

#Para acceder a los valores de las listas:

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
# print(my_other_list[4]) Index error - Esta por fuera de la cantidad de indices
# print(my_other_list[-5]) Index error - Se pasa de la cantidad de indicens

# Si le aplicamos .count(argumento) cuenta la cantidad de ocurrencias del argumento que le pasamos. 
print(my_other_list.count("Rovaretti"))
print(my_list.count(35))

age, height, name, surname = my_other_list #hay que darle la cantidad de variables como de elementos de la lista a desempaquetar
print(name, surname)
print(age)

# ordenamos 
surname, name, age, height  = my_other_list[3], my_other_list[2], my_other_list[0], my_other_list[1]

# Concatenacion de listas
print(my_list + my_other_list)

""" Python no puede definir variables como Constantes. 
Para dar a entender se usa el nombre en mayusculas.
CONST_NAME = ...
"""
# Operaciones

my_other_list.append("Ipa")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_list.remove(35) #elimina el elemento por el dato en concreto
print(my_list)

my_new_list = my_list.copy()

my_list.pop() #elimina el ultimo elemento de la lista
my_list.pop(2) #elimina un elemento en el index q le señalamos
print(my_list)

del my_list[0]
print(my_list)

my_list.clear() #vacia la lista
print(my_list)

my_other_list[1] = "Azul"
print(my_other_list)

print(my_new_list)
my_new_list.reverse() # Invierte el orden de los index
print(my_new_list)

my_new_list.sort() #ordena por defecto de menor a mayor, o alfabeticamente

print(my_new_list)
