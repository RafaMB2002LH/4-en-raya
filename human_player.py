#Esta clase define el jugador humano
class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    #Esta funcion pide los movimientos al humano   
    def human_move(self, state):
        # Entrada del usuario
        while True:
            square = int(input("Ingresa el número de la casilla para colocar tu ficha (1-16): "))
            print()
            if state[square - 1] == "-":
                break
        return square - 1
