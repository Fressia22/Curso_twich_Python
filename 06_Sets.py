# SETS

my_set = set()
my_other_set = {} #se define con {}, igual q un diccionario. Si lo dejamos vacío lo va a interpretar como 'tipo dict'

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Fabrina", "Rovaretti", 35, 1987}
print(type(my_other_set)) #si colocamos datos en {} ya nos toma el 'class set'

# Operaciones
print(len(my_other_set))

print(my_other_set)

#print(my_other_set[2]) #sets no son estructuras ordenadas, por tanto no podemos consultar index específico

my_other_set.add("Azul") #no añade ordenadamente
print(my_other_set)

my_other_set.add("Azul") #no admite repeticiones
print(my_other_set)

print("Rojo" in my_other_set) # devuelve bool si existe el dato o no
print("Azul" in my_other_set)

my_other_set.remove(1987)
print(my_other_set)

my_other_set.clear() # con clear vaciamos de elementos la variable, pero sigue viva
print(len(my_other_set))

del my_other_set # al borrarla directamente no existe mas la variable
#print(my_other_set)

# Hacer conversiones a list o tupla es riesgoso porque no sabemos donde nos va a ubicar los datos
my_set = {"Georgina", 30, 1.61}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # la 1ra iteracion nos tira un dato en el index#0
print(my_list[0]) # la 2da iteracion nos tira otro dato en el index#0

my_other_set2 = {"Shakira", "skate", 1992}

# podemos unir 2 o massets
my_new_set = my_set.union(my_other_set2)
my_new_set.union(my_set) #la union con my_set la ignora porque no hay elementos nuevos
print(my_new_set) #la union con my_set la ignora porque no hay elementos nuevos
print(my_new_set.union({"Agroecologa", "60"})) #la union con nuevos datos la toma

print(my_new_set.difference(my_set)) #muestra los elementos que se difencian de otro set

