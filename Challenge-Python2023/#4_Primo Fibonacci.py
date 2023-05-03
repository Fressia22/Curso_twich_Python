"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
 """
numero_elegido = int
#numeros_primos = list(2, 3, 5, 7, 11, 13, 17,)
def que_soy(numero_elegido:int=2):

    divisor = 1

    while divisor < numero_elegido:
        #print(divisor)
        divisor += 1
        
        if numero_elegido % 2 == 0:
            print(f"{numero_elegido} dividido {divisor} Es Par y NO es primo")
            

        if numero_elegido % 2 != 0:
            print(f"{numero_elegido} dividido {divisor} Es Impar")
             
        else:
                continue
    
        if numero_elegido == divisor and numero_elegido % 2 != 0:
                print(f"{numero_elegido} es numero primo")
            

            

    
    print("Se terminó la función")

"""
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es justo 15. Se detiene la ejecución!")
        # Se cumple la condición del While pero podemos ROMPER el bucle cuando se cumple una condición intermedia.
        break
   
    print(my_condition) #ESTO no se va a ejecutar cuando el break rompa el ciclo
    
print("La ejecución sigue continuando")

"""


    #divisor == 1
    #print(divisor)
"""
    for divisor in numero_elegido:
        divisor += 1
        print(divisor)
        if (numero_elegido / divisor) == 1:
            print(f"{numero_elegido} es numero primo")
                
        if numero_elegido % divisor == 0:
            print(f"{numero_elegido} dividido {divisor} NO es primo")
            
        if divisor > numero_elegido:
                  break
    else:
             print("Se paró")
"""
#    return:
#        print(f"{numero_elegido} {} es primo, {} es fibonacci y es {}")

# Cuando es fibonacci


# Cuando es par
#numero_elegido % 2 == 0

que_soy(15)
