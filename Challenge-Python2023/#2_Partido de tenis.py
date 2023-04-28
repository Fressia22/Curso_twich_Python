"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""
#Usamos la funcion interna de Python Enumerate para controlar que los datos que entren 
#pertenezcan a la clase Player, y no se ingersen otros datos inesperados o incorrectos
#(x ej. "P5" o "P")
from enum import Enum
class Player(Enum):
    P1 = 1
    P2 = 2

def tenis_game(points: list):
    
    game = ["Love", "15", "30", "40","Fin del partidoo"]
    p1_points = 0
    p2_points = 0
    finished = False
    error = False
    
    for player in points:

        error = finished
        
        p1_points += 1 if player == Player.P1 else 0
        p2_points += 1 if player == Player.P2 else 0

        #Control de la situacion de empate y ventaja
        if p1_points >= 3 and p2_points >= 3:
            if abs(p1_points - p2_points) <= 1:
                print("Deuce" if p1_points == p2_points else
                  "Ventaja P1" if p1_points > p2_points else "Ventaja P2")
            else:
                finished = True
        else:
            if p1_points <= 3 or p2_points <= 3:
                #Aca manda a imprimir según el index q le indique la cantidad de puntos q tiene, ubica el rotulo en el listado game
                print(f"{game[p1_points]} - {game[p2_points]}")
            else:
                finished = True

    print("Los puntos jugados no son correctos" if error else
          "Ha ganado el P1" if p1_points > p2_points else
           "Ha ganado el P2" if p2_points > p1_points else "El juego no ha terminado")    
"""
        if player == Player.P1:
            p1_points += 1
        elif player == Player.P2:
            p2_points += 1
"""


#Por ultimo pasamos el listado de los puntos que ocurrieron y los ubicamos en su clase
tenis_game([Player.P1, Player.P1, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1])

#Observación: el control de error no esta bien hecho, porque al introducir más puntos para 1 solo jugador da error, 
# y cuando la ventaja es para 1 pero estando a diferencia de ventajas no avisa q ha termido a tiempo