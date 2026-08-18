j1=input("jugador 1 elije una acción:")
j2=input("jugador 2elije una acción:")

if j1==j2:
    print("empate")
elif j1=="piedra" and j2=="tijera":
    print("jugador 1 gana")
elif j1=="tijera" and j2=="papel":
    print("jugador 1 gana")
elif j1=="papel" and j2=="piedra":
    print("jugador 1 gana")
