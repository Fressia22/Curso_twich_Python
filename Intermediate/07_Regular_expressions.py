# EXPRESIONES REGULARES #

# Hay un modulo del sistema llamado RE (R-egular E-xpressions)
import re 

"""
 - - - - - - - - - - - - - - -
 re.match()
 - - - - - - - - - - - - - - - -

uno de los metodos mas utilizados es MATCH para comprobar si en una cadena de texto dada
aparece cierta fórmula (concatenación de strings) / expresiones regulares.
OJO: la búsqueda de coincidencia parte siempre del principio de la cadena/caracter 0, si la 
muestra aparece en otro lugar nos dará NONE
Consola:
<re.Match object; span=(0, 22), match='Ésta es la lección n°7'>
"""
my_string = "Ésta es la lección n°7: Lección sobre Expresiones regulares."

my_other_string = "Ésta no es la lección n°6: Manejo de ficheros."

my_match = re.match("Ésta es la lección n°7", my_string, re.I) #recibe la muestra en string, la cadena donde buscar, y se puede setear parametros de coincidencia predados
print(my_match) #--> si COINCIDE nos devuelve información de rango donde se haya y texto coincidente
                 #--> si NO COINCIDE nos devuelve None

# Para printear la coincidencia podemos usar SPAN que nos devuelve el rango de coincidencia en una tupla de 2 valores
#  y lo alojamos en 2 variables: principio y fin,
start, end = my_match.span() 

print(my_string[start:end]) # Luego printeamos a partir de la cadena de texto delimitando con esas variables

""" Cuando no hay coincidencia, devuelve NONEType, y da error de atributo para el método SPAN
asi que hay que controlarlo con IF: 
"""

my_match = re.match("Ésta no es la lección", my_other_string, re.I)
if my_match != None: # Una forma: con Diferente <!=>
#if my_match is not None: # Otra forma: con <is not>
#if not(my_match == None): # Tercera forma <not()>
    print(my_match)
    start, end = my_match.span()
    print(my_other_string[start:end])
else:
    print("! No hay match")

"""
 - - - - - - - - - - - - - - -
 re.search()
 - - - - - - - - - - - - - - - -

SEARCH de forma similar comprobará si en una cadena de texto dada aparece cierta fórmula (concatenación de strings) / expresiones regulares.
La diferencia con match: la coincidencia pude hayarse en CUALQUIER PATE de la cadena, 
La diferencia con findall: solo buscará hasta hallar la 1ra coincidencia (por más que haya más apariciones)
Recibe los mismos argumentos y devuelve el match/None.
Consola:
<re.Match object; span=(11, 22), match='lección n°7'>
"""

my_search = re.search("lección n°7", my_string, re.I)
if my_search is not None:
    print(my_search)
    start, end = my_search.span()
    print(my_string[start:end])
else:
    print("! No coincide la búsqueda")


"""
 - - - - - - - - - - - - - - -
 re.findall()
 - - - - - - - - - - - - - - - -

FINDALL Recibe los mismos argumentos como las demás, pero no devuelve [rango] ni NONETYPE sino... 
La diferencia: NO devuelve un rango, sino un LISTADO de TODAS las coincidencias que ocurran en la búsqueda,
            Tampoco devuelve NONE, en caso de no hallar coincidencia el listado quedará vacío: <[]>
Consola: 
['lección', 'lección']
"""

my_findall = re.findall("lección", my_string, re.I)
print(my_findall)

"""
 - - - - - - - - - - - - - - -
 re.split()
 - - - - - - - - - - - - - - - -

SPLIT Busca un patrón dado y a partir de ese punto nos divide la cadena en una lista de 2 partes/elementos.
Consola: 
['Ésta es la lección n°7', ' lección sobre Expresiones regulares.']
<class 'list'>
"""
my_split = re.split("\n", my_string) 
#my_split = re.split(":", my_string) 
print(my_split)
print(type(my_split))

# si no halla el criterio, devuelve la cadena sin dividir en una lista de 1 elemento.

"""
 - - - - - - - - - - - - - - -
 re.sub()
 - - - - - - - - - - - - - - - -

SUB es para sustituir un tramo de cadena por otro str.
Consola: 
Ésta es la lección n°7:
Lección sobre RegEx.
"""

my_sub = re.sub("Expresiones regulares", "RegEx", my_string)
print(my_sub) # Devuelve la cadena de str modificada

# Con el PIPE <|> podemos concatenar varias apariciones para reemplazar con el criterio.
my_sub = re.sub("lección|Lección", "lexión", my_string)
print(my_sub)

my_sub = re.sub("[l|L]ección", "LECCIÓN", my_string) # Tambien puede darse ambas alternativas entre corchetes con pipe <[|]>
print(my_sub)


"""
 - - - - - - - - - - - - - - - - - - - - - - -
 PATTERNS más específicos de RegExp oficiales
 - - - - - - - - - - - - - - - - - - - - - - -

Las expresiones regulares son propias de cualquier lenguaje de programación
Ej:
[a-c] --> buscará a, b, ó c
[a-z] --> buscará cualquier caracter entre a y z minúscula
[0-9] --> buscará cualquier número entre 0 y 9
[a-zA-Z0-9] --> buscará cualquier caracter minúscula, mayuscula o numeros

[\] --> se usa para escapar caracteres especiales
    \d --> match cuando el str contiene digitos
    \D --> match cuando el str NO contiene digitos

[.] --> cualquier caracter (excepto newline <\n> caracter)

[*] --> zero, o más veces
[?] --> zero, o UNA vez
[+] --> UNA, o más veces


[^] --> que empiece con xcriterio
[$] --> que termine con xcriterio

[|] --> para enumerar uno u otro

{3} --> exactamente 3 caracteres
{3,8} --> de 3 a 8 caracteres

...y hay muchas.
También se pueden utilizar códigos unicode.
"""

my_pattern = r'[lL]ección'
print(re.findall(my_pattern, my_string)) # Enlista las coincidencias ya sea con 'L' o con 'l'  

my_pattern = r'[lL]ección|Expresiones'
print(re.findall(my_pattern, my_string)) # Enlista las coincidencias ya sea con el primer criterio y con el segundo

my_pattern = r"[0-9]"
print(re.findall(my_pattern, my_string)) # Enlista numeros que haya encontrado en el rango

print(re.search(my_pattern, my_string)) # <re.Match object; span=(21, 22), match='7'>

my_pattern = r"\d"
print(re.findall(my_pattern, my_string)) # Enlista los caracteres numericos que haya encontrado en el rango

my_pattern = r"\D"
print(re.findall(my_pattern, my_string)) # Enlista los caracteres NO numericos que haya encontrado en el rango

my_pattern = r"[l]."
print(re.findall(my_pattern, my_string, re.IGNORECASE)) # Enlista las palabras q empiezan en 'l' y su caracter consiguiente.

my_pattern = r"[:].*"
print(re.findall(my_pattern, my_string, re.IGNORECASE)) # Enlista todo lo q sigue a partir de los ":" 

# un patrón para buscar match de formato válido de email:
my_email = "fabri_music.1987@gmail.com" 

my_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"

print(re.match(my_pattern, my_email)) # --> Matcheará si la cadena comienza coincidiendo con el patron
print(re.search(my_pattern, my_email)) # --> Searcheará si el patron aparece en cualquier parte de la cadena
print(re.findall(my_pattern, my_email)) # --> Enlistará todas las coincidencias con el patrón
# ! todas estas funciones aplican si la variable es una cadena de string, no LISTAS u otros objetos.

my_email = "geo_rgina.92@gmail.gob.edu"
print(re.findall(my_pattern, my_email))

# https://regex101.com