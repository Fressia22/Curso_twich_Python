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
my_string = "Ésta es la lección n°7:\nLección sobre Expresiones regulares."

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

SUB Busca un patrón dado y a partir de ese punto nos divide la cadena en una lista de 2 partes/elementos.
Consola: 
['Ésta es la lección n°7', ' lección sobre Expresiones regulares.']
<class 'list'>
"""