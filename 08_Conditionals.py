# Condicionales

my_condition_T = True
my_condition_F = False

# para que la condición del if se cumpla tiene q ser True 
if my_condition_T:
    print("Se ejecuta la condición del if True")

if my_condition_F:
    print("Se ejecuta la condición del if False")

my_condition = 1

if my_condition == 10:
    print("Se ejecuta la 1ra condición comparativa")

if my_condition > 10:
    print("Es mayor que 10")
# else es el caso por defecto, si no se ucmple nada del if, cierra con esto.
else:
        print("Es menor o igual que 10")

# Se puede concatenar condiciones con "and, or, not"
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor igual que 20")

print("La ejecución continúa...")

# Si tenemos un string vacío nos lo da como False.
my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto no está está vacía")

# Podemos usar not para invertir el valor
my_string = ""

if not my_string:
    print("Mi cadena de texo está vacía")