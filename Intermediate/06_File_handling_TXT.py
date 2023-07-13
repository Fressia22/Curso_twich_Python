# FILE HANDLING (Archivos *.txt, *.json, *.html)

""" - - - - - - - - - - - - - - -
 Manejo de *.txt files
 - - - - - - - - - - - - - - - - """

import os
#poner correctamente la ruta del archivo desde el directorio raiz y entre comillas ""!
# y el modo de escritura/lectura

txt_file = open(".\my_file.txt", "w+")
txt_file.write("Me llamo Fabrina\nMi apellido es Rovaretti\nTengo 35 años\nMi lenguaje preferido es Python")

#txt_file.close()

with open(".\my_file.txt", "r+") as my_other_file:
    #print(my_other_file.read())
    #print(my_other_file.read(13))
    #print(my_other_file.readline())
    #print(my_other_file.readline()) # lee la siguiente linea que queda
    for lines in my_other_file.readlines():
        print(lines)

my_other_file.write("\naunque tambien me gusta Golang.")
print(my_other_file.readline())
"""
txt_file.close()

with open("./my_file.txt","+a") as my_other_file:
    my_other_file.write("\n...y no nos olvidemos de Solidity.")


# Tambien podríamos eliminarlo en el final del programa
#os.remove("./my_file.txt")

"""