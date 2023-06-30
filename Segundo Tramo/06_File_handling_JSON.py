""" - - - - - - - - - - - - - - -
 Manejo de *.json files
- - - - - - - - - - - - - - - - """

#Importamos un modulo dedl core de Python para trabajar con Json
import json

json_file = open("./my_file.json","w+") #este modo de escritura intentará siempre crear el fichero desde cero.


# un jason tiene una estructura similar a la de un dictionary, asi que lo manejamos como tal (las keys han de ser str) y los aglomerados han de ser [listas]
json_test = {
    "Nombre":"Daniel", 
    "Apellido":"Rovaretti",
    "Edad":"61",
    "Lenguajes":["Python", "Golang", "JavaScript"],
    "Website":"https://@reina.fabrina.com"
    }

#json_file.write("Viva la Pepa!") # la funcion write solo recibe un str
# Dump recibe un parametro/objeto
json.dump(json_test, json_file, indent=4) # La identacion formatea con nuevas lineas y le definimos la distancia de espacios en cada elemento

# si vuelvo a dumpear añade todo a continuación de lo anterior
#json.dump(json_test, json_file, indent=4)

json_file.close()

with open("./my_file.json") as my_other_file:
    for lines in my_other_file.readlines():
        print(lines)

# Hasta ahi pudimos crear, escribir y leer un json,
# a la inversa, si ya tuvieramos un archivo dado, se traduce como objeto dict
json_dict = json.load(open("./my_file.json"))

print(json_dict)
print(type(json_dict))
print(json_dict["Lenguajes"])
