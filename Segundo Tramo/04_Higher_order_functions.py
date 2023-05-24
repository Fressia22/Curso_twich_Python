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
