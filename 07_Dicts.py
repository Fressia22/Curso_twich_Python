# Dictionaries_ Estructura de items con relación Llave:Valor

my_dict = dict()
print(type(my_dict))
    
my_other_dict = {}
print(type(my_dict))

my_other_dict = {"Nombre":"Fabrina", "Apellido":"Rovaretti", "Edad":35, 1:"Golang", 2:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Daniel", 
    "Apellido":"Rovaretti",
    "Edad":61,
    "Lenguajes":{"Python","Javascript","html"},
    2023: "Nuevos aprendizajes"
    }

print(my_dict)
print(len(my_dict)) # Cuenta LLAVES, NO CUENTA valores

print(my_dict["Nombre"]) #
my_dict["Nombre"] = "Georgina"
print(my_dict["Nombre"])

my_dict["Domicilio"] = "Caseros 5634"
print(my_dict)

del my_dict["Lenguajes"] # Para borrar un item
print(my_dict)

print("Rovaretti" in my_dict) # Da False porque no busca en los datos
print("Apellido" in my_dict) # Da True porque en realidad BUSCA EN LAS LLAVES

print(my_dict.items()) # Dicta los items con llave y sus correspondientes valores
print(my_dict.keys()) # Lista todas las keys
print(my_dict.values()) # Lista todos los valores sueltos

#Crear un diccionario con KEYS pero sin valores
my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Edad", "Altura")) #1 poniendo keys a mano
print(my_new_dict)

my_keys_list = ["Nro de usuario", "DNI", "mail"] #2 usando una lista de keys
my_new_dict2 = dict.fromkeys((my_keys_list))
print(my_new_dict2)

my_new_dict2 = dict.fromkeys(my_dict) #3 Tomando las keys desde otro diccionario ya hecho. EL USO MAS EFICAZ
print(my_new_dict2)
# la funcion .fromkeys puede recibir un segundo argumento que pone un mimsmo VALOR en todos los items.

# No tiene mucho sentido convertir un diccionario ni en lista, tupla o set, porque solo nos traduce las keys sin valores. 
# Si queremos una lista de los valores que almacena un diccionario:
print(list(my_dict.values()))


