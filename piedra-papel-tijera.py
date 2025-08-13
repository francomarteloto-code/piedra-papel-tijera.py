#Datos de los jugadores
nombre1 = input("Jugador 1, ingresa tu nombre: ")
nombre2 = input("Jugador 2, ingresa tu nombre: ")

#Contadores de victorias
puntos_jugador1 = 0
puntos_jugador2 = 0
ronda = 0

#Opciones del juego
opciones = ["piedra", "papel", "tijera"]

#Bucle/loop del juego: Maximo 3 rondas o hasta que un jugador llegue a 2 puntos
while ronda < 3 and puntos_jugador1 < 2 and puntos_jugador2 <2:
    jugador1 = input(f"{nombre1}, elige piedra, papel o tijera: ").lower().strip()
    jugador2 = input(f"{nombre2}, elige piedra, papel o tijera: ").lower().strip()

    #Validación de entradas: si alguna es invalida, no se contabiliza la ronda
    if jugador1 not in opciones or jugador2 not in opciones:
        print("Entrada invalida. Por favor, elige entre piedra, papel o tijera.")
        continue
       
    #Condiciones:
    
    condition1 =(jugador1 == "piedra" and jugador2 == "tijera")
    condition2 =(jugador1 == "papel" and jugador2 == "piedra")
    condition3 =(jugador1 == "tijera" and jugador2 == "papel")

    if jugador1 == jugador2:
        print("¡Es un empate!")
    elif  condition1 or condition2 or condition3:
        print("Ha ganado:",nombre1)
        puntos_jugador1 += 1
    else:
        print("Ha ganado:",nombre2)
        puntos_jugador2 += 1

    ronda += 1
    print(f"Marcador actual: {nombre1} {puntos_jugador1} - {nombre2} {puntos_jugador2}")

#Resultados finales
print("=== Resultado Final ===")
if puntos_jugador1 > puntos_jugador2:
   print(f"¡{nombre1} ha ganado el juego con {puntos_jugador1} puntos!")
elif puntos_jugador2 > puntos_jugador1:
    print(f"¡{nombre2} ha ganado el juego con {puntos_jugador2} puntos!")
else:
    print("¡El juego ha terminado en empate!")


