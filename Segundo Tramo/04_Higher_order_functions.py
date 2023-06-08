# HIGHER ORDER FUNCTIONS - Funciones que son capaces de ejecutar funciones.

# Aquí mostramos como  puede una función tener otra embebida:
def sum_one(value):
    return value + 1

def sum_values_and_add_one(fist_value, second_value):
    return sum_one(fist_value + second_value)

print(sum_values_and_add_one(2, 5))

# Pero de orden mayor pasa a ser si la usamos así, pasando de parametro una función u otra:
def sum_five(value):
    return value + 5

def sum_values_and_add_value(fist_value, second_value, f_sum):
    return f_sum(fist_value + second_value)
# En este caso el parametro f_sum recibirá cualquier función que nosotros queramos y puede cambiar, 
# pero la estructura de la función de orden mayor queda armada estática

print(sum_values_and_add_value(2, 5, sum_one))
print(sum_values_and_add_value(2, 5, sum_five))


# CLOSURES - Es una función que retorna una función (no un valor, ni un calculo)

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value #el original value se guarda el contexto
    return add

add_closure = sum_ten(1)
print(add_closure(5))

# Tambien podemos llamarla concatenando las funciones, sum_ten devuelve una función (add) que le suma el 2do parametro cargado. 
print((sum_ten(20))(5))

# Built-in HIGHER ORDER FUNCTIONS

iterable_item = [2, 5, 10, 22, 3, 30]
# MAP 
# Recibe 1 funcion operadora y un elemento iterable sobre el que aplicar esa función, 
# Devuelve otro listado con cada valor operado)

def multiply_two(value):
    return 2 * value

print(f"{list(map(multiply_two, iterable_item))} MAP con funcion definida *2")

# En vez de una funcion definida tambien puedo pasarle una lambdas:
print(f"{list(map(lambda value: value * 3, iterable_item))} MAP con lambda *3")

# FILTER
# Va a solicitar una función que retorne un True or False
# Devuelve otro listado habiendo recorrido y filtrado segun cuando la función devolvuelva True
def filter_greater_than_ten(value):
    if value > 10:
        return True
    return False
"""
Esta función podría resumirse en:
def filter_greater_than_ten(value):
        return value > 10
"""
# Devuelve un nuevo listado filtrado con el criterio de la función
print(f"{list(filter(filter_greater_than_ten, iterable_item))} FILTER con función mayor q 10")

# Filter con LAMBDA en vez de función:
print(f"{list(filter(lambda value: value > 10, iterable_item))} FILTER con LAMBDA mayor q 10")

# REDUCE 
# (Esta dentro de un módulo llamado "functools")
from functools import reduce

def sum_two_values(first_value, second_value):
    print(f"Toma como 1st value: {first_value}")
    print(f"Toma como 2nd value: {second_value}")
    return first_value + second_value 
    # Va reemplazando como 1st value su resultado de la suma anterior, 
    # y utiliza del listado a iterar el 2nd value para ir sumando hasta 
    # reducir el listado a 1 unico valor resultado de la suma de todos los items con su anterior (según indicó la función).


print(f"{reduce(sum_two_values, iterable_item)} --> Resultado de REDUCE con función")

print(f"{reduce(lambda first_value, second_value: first_value + second_value, iterable_item)} --> Resultado de REDUCE con LAMBDA")