"""
*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""
import random

def password_gen(length=8, capital=False, numbers=False, symbols=False):
    #armo una variable para el rango de caracteres desde el que elegir 
    characters = list(range(97, 123))
    
    #Casuisica:
    if capital == True:
        characters += list(range(65, 91))

    if numbers == True:
        characters += list(range(49, 58))

    if symbols == True:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))
    
        
    #una variable para contener las iteraciones de cada elección
    password = ""

    final_lenght = 8 if length < 8 else 16 if length > 16 else length
    #ciclo while para iterar con condicion: la cantidad de caracteres(longitud de contraseñal)
    while len(password) < final_lenght:
        #seleccionar una letra de forma aleatoria con un modulo llamado RANDOM y añadirla a la variable password
        #chr es una funcion de python que ubica el codigo ascii
        password += chr(random.choice(characters))

    return password

"""
#Casuisica:
    if capital == True:
        characters += list(range(65, 91))

    if numbers == True:
        characters += list(range(49, 58))

    if symbols == True:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))


"""

# casos de prueba:
print(f"Por defecto sin pasar configuraciones --> {password_gen()}")
print(f"Pasando: length=16 --> {password_gen(length=16)}")
print(f"Pasando: length=1 --> {password_gen(length=1)}")
print(f"Pasando: length=22 --> {password_gen(length=22)}")
print(f"Pasando: length=12, capital=True --> {password_gen(length=12, capital=True)}")
print(f"Pasando: length=12, capital=True, numbers=True --> {password_gen(length=12, capital=True, numbers=True)}")
print(f"Pasando: length=12, capital=True, numbers=True, symbols=True --> {password_gen(length=12, capital=True, numbers=True, symbols=True)}")

# Podria mejorarse haciendo un control preliminar de si password resultante contiene genuinamente al menos 1 simbolo de lo que se activó en True