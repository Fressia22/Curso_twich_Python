# STRINGS
# se pueden usar "comillas dobles" y 'simples' indistintamente
# se usan "\" antes de comillas como escape de la interpretacion del comando, y deja el caracter escrito literal
my_string = "Mi string"
my_other_string = 'Mi otro string'
my_scape_string = "Me dijo \"Don\'t touch! portate bien\""
print(my_scape_string)

# len mide la cantidad de caracteres dentro del str
print(len(my_string))
print(len(my_other_string))

# Concatenacion de Str
print(my_string + " " + my_other_string)

# Saltos y tabulaciones
my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

# Formateo eficaz con "f", ".format" y con "%s = string; %d = numeros reales; %f = float"

name, surname, age = "Fabrina", "Rovaretti", 35
#1 con .format, nos traes el dato tal cual
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

#2 con %_ le damos formato mas propiamente dicho 
# %s = string; %d = numeros reales; %f = float
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

#3 interpolacion f-strings
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division (porcion) 
# desde index 0 :(hasta) index X(no inclusive)
language_slice = language[1:3] #saltea el index #0(P) y tira el #1(y), el #2(t); y no nicluye el #3(h)
print(language_slice)
language_slice = language[1:]  #saltea el index #0(P) y tira del #1(y) hasta #final incluido
print(language_slice)
language_slice = language[-2] #cuenta de atras para adelante a partir del -1
print(language_slice)
language_slice = language[0:6:3] #elegir solo algunos caracteres
print(language_slice)

reversed_language = language[::-1] # Al reves
print(reversed_language)

# FUNCIONES
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric()) # devuelve un bool
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper()) # devuelve un bool
print(language.startswith("py")) # devuelve un bool
