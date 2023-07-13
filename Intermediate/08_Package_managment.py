# MANEJO DE PAQUETES en PYTHON #

""" - - - - - - - -
PIP

Python package manager

https://pypi.org
- - - - - - - - -

Modulos conocidos: Pandas, Numpy, login.

DESDE CONSOLA:

1°) Comprobar si tenemos PIP: 
<pip --version>

2°) Si no lo tenemos, hay que instalarlo:
<pip install pip>

O actualizarlo:
<pip install --upgrade pip>

3°) Buscamos un paquete:
<pip install numpy>
"""
import numpy

print(numpy.version.version)

numpy_array = numpy.array([32, 73, 59, 31, 98])
print(type(numpy_array)) # <class 'numpy.ndarray'>

print(numpy_array *2)


""" - - - - - - - 
pip list
- - - - - - - 
<pip list>
Te muestra la lista de todas las librerias que tenemos instaladas

<pip uninstall pandas>
Desinstalar alguna libreria

<pip show numpy>
tira info sobre la libreria y sus autores
"""

# <pip install requests> Una librería para
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=51")
print(response)
print(response.status_code)
print(response.json())
