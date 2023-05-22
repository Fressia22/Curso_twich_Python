"""
Reto #0
EL FAMOSO "FIZZ BUZZ"
 * Dificultad: FÁCIL
Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 
(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 Información adicional:
 - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

def fizz_buzz():
    for index in range(1, 101):
        
        if index % 3 == 0 and index % 5 == 0:
            print("fizz-buzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

#fizz_buzz()

"""
Reto #1
¿ES UN ANAGRAMA?
Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean)
según sean o no anagramas.
 Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 NO hace falta comprobar que ambas palabras existan.
 Dos palabras exactamente iguales no son anagrama.
 
"""

def es_anagrama(word_1: str, word_2: str):
    if word_1.lower() == word_2.lower():
        return False 

    return sorted(word_1.lower()) == sorted(word_2.lower())

#print(es_anagrama("Fabrina", "afarbin"))

# 1ro Controla que si es la misma palabra de false.
# 2do Controla que tome todo en mayuscula o minuscula por igual con language.Lowercase
# 3ro ordenar las palabras en orden alfabetico y compararlas

"""
Reto #2
LA SUCESIÓN DE FIBONACCI
 * Dificultad: DIFÍCIL

Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    # inicializamos en 0 y 1 que es como empieza la serie
    prev = 0
    next = 1

    for index in range(1, 51):
        print(f"Vuelta #{index} {prev}")

        fib = prev + next
        prev = next
        next = fib


#fibonacci()

"""
Reto #4
¿ES UN NÚMERO PRIMO?
* Dificultad: MEDIA

Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():

    for number in range(1, 101):
        # Primo es un numero mayor que 1
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
        
            if not is_divisible:
                print(number)

#is_prime()

"""
Reto #6
INVIRTIENDO CADENAS
 * Dificultad: FÁCIL
Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje
que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(frase: str):
    len_frase = len(frase)
    frase_invertida = ""
    
    for index in range(0, len_frase):
        frase_invertida += frase[len_frase - index - 1]
    
    return frase_invertida

print(reverse("Hola Mundo!"))