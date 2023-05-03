"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 """
# MoureDev resuelve de simple a complejo:
# 1 - Si espar o impar
# 2 - Si es primo o no
# 3 - Formula matemática para Fibonacci
def check_prime_fibonacci_even(number):
    
    result = f"{number} "
    
   

    # PRIMO (nro natural mayor que 1 divisible entre 1 y sigo mismos)
    if number > 1:
        for index in range(2, number):
            if number % index == 0:
                result += "no es primo, "
                break
        else:
            result += "es primo, "
    else:
        result += "no es primo, "   
    
    # FIBONACCI



    # PAR (si el modulo del numero es = a 0, o si el resto de la div / 2 da de resto 0)
    """
    if number % 2 == 0:
        result += "y es par."
    else:
        result += "y es impar."        
    
    Esto mismo dicho en 1 sola linea puede ser asi:
    """
    result += "y es par." if number % 2 == 0 else "y es impar."

    print(result)

    