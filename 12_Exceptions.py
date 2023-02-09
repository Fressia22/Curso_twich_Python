# EXCEPTION HANDLING #
"""
try: Run this code.
except: Execute this code when there is an exception.
*else: NO EXCEPTIONS? Run this code.
*finally: Always run this code.
(*opcional)
"""
numberOne = 5

numberTwo = 1
numberTwo = "1"

# Minimo necesario para atajar errores: Try , except
try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")

# Opcional continuar con: else, finally:

try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except: # se ejecuta si se produce una excepción
    print("Se ha producido un error")
else: #se ejecuta si no se produce ninguna excepción
    print("La ejecución continúa correctamente")
finally: #se ejecuta siempre
    print("El programa ha finalizado (o sigue corriendo sin haber sucumbido al error)")

# CAPTURA DE ERRORES POR TIPO
try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
except ValueError: # solo controla los errores de tipo Value
    print("Se ha producido un ValueError")
except TypeError: # solo controla los errores de tal tipo
    print("Se ha producido un TypeError")

# CAPTURA DE INFO DE LA EXCEPCION
try:
    print(numberOne + numberTwo)
    print("No se ha producido ningun error")
# convertimos la info de error en un objeto para poder imprimirlo
except ValueError as my_value_error: #este error esta especificamente controlado (pero no es nuestro error)
    print(f"Ups! un value malió sal: {my_value_error}")
except Exception as my_other_exception: # si el error es de cualquier otro tipo guardamos Exception
    print(f"Ups! alguna cosa malió sal: {my_other_exception}")
