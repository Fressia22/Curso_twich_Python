# OPERADORES ARITMETICOS

print("Hola" + "Hola")
print("Hola " * 5)

# Para concatenar 
# un dato str y un dato int
print("Hola" + str(5))
# Solo puede * multiplicar str por enteros
my_float = 2.5 * 2
print("Hola\n" * int(my_float))

# Orden de los terminos se separa con +, - ; y en los subterminos las operaciones *, **, /, //, % se pueden separar con ().
print(2 * 3 ** 3 / 54 + 10)

# OPERADORES COMPARATIVOS #

print(3 > 4)
print(3 >= 4)
print(3 < 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Compara los str por ordenacion alfabetica por ASCII
print("Hola" > "Python")
print("Hola" >= "Python")
print("Hola" < "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")


""" OPERADORES LOGICOS con lógica booleana: and, or, not
and (&&):
true and true = True
true and false = False
false and false = False
or (||):
true or true = True
true or false = True
false or false = False
not (!=)
True = False
false = True

"""

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
#podemos concatenar con parentesis que dan prioridad
print(3 < 4 or ("Hola" > "Python" and 4 == 4j))
# NOT se utiliza para que devuelva el contrario de 1 resultado
print(not(3 > 4))


