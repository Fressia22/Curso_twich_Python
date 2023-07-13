#   LAMBDAS 
# Son como funciones anónimas (no tiene nombre) se crean con:
# la palabra reservada lambda, los parametros que recibe y lo que tiene que hacer,
# Todo en una sola linea!

lambda first_value, second_value: first_value + second_value

# Para poder llamarla, podemos encapsularla en una variable:
sum_two_values = lambda first_value, second_value: first_value + second_value

# Para hecharla andar le añadimos parentesis al nombre de la variable y recibe y opera los datos
print(sum_two_values(2, 5))

# (es como otro modo de desarrollar una función, más pequeña funcional al bloque del código del momento, 
# y no tanto con uso a nivel general)

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 5))

# Puedo embeberla dentro de una función tambien:

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


# Para pasarle los parámetros hay que hacerlo dentro del llamado,  al lado de los parametros de la función.

print(sum_three_values(55)(2, 5))
# El  55 responde a value, el 2 es first_value y el 5 second_value