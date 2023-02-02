# Functions
"""
Llamamos un bloque de código que siempre está en el mismo lugar y así ahorramos reescribir código una y otra vez.
Palabra reservada: def
Todo lo que tabulamos a la derecha despues de la definicion de la funcion es el bloque de código de la función.
"""
def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values (first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5,7)
sum_two_values("5","7")

my_result = sum_two_values(2, 8)
print(my_result)

def sum_two__values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two__values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"Hola! Soy {name} {surname}")

print_name(surname="Rovaretti", name="Fabrina")

def print_name_with_default(name = "Sin Nombre", surname= "Sin apellido", alias = "Sin alias"):
    print(f"Hola! Soy {name} {surname}, y mi alias es: {alias}")

print_name_with_default(alias="Flakira", surname="Rovaretti", name="Fabrina")
# Si no le ingresan toda la info, va el value por default:
print_name_with_default(alias="Flakira", name= "Fabrina")

def print_upper_texts(*texts):
    
    for text in texts:
        print(text.upper())
        

print_upper_texts("Hola", "Python", "Me pasaron a mayúsculas")