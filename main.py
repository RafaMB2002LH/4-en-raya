import tkinter as tk
from tkinter import messagebox

class JuegoCuatroEnRaya:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("4 en Raya")

        # Inicializar el turno del jugador
        self.turno_jugador = "X"

        # Crear botones para el tablero
        self.botones = [[None, None, None, None] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                self.botones[i][j] = tk.Button(ventana, text="", font=("Helvetica", 16), width=5, height=2, command=lambda i=i, j=j: self.hacer_movimiento(i, j))
                self.botones[i][j].grid(row=i, column=j)

    def hacer_movimiento(self, fila, columna):
        # Verificar si la celda está vacía
        if self.botones[fila][columna]["text"] == "":
            # Realizar el movimiento
            self.botones[fila][columna]["text"] = self.turno_jugador

            # Verificar si hay un ganador
            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.turno_jugador} gana!")
                self.reiniciar_juego()
            elif self.empate():
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.reiniciar_juego()
            else:
                # Cambiar el turno del jugador
                self.turno_jugador = "O" if self.turno_jugador == "X" else "X"

    def verificar_ganador(self):
        # Verificar filas y columnas
        for i in range(4):
            if (self.botones[i][0]["text"] == self.botones[i][1]["text"] == self.botones[i][2]["text"] == self.botones[i][3]["text"] != "") \
                    or (self.botones[0][i]["text"] == self.botones[1][i]["text"] == self.botones[2][i]["text"] == self.botones[3][i]["text"] != ""):
                return True

        # Verificar diagonales
        if (self.botones[0][0]["text"] == self.botones[1][1]["text"] == self.botones[2][2]["text"] == self.botones[3][3]["text"] != "") \
                or (self.botones[0][3]["text"] == self.botones[1][2]["text"] == self.botones[2][1]["text"] == self.botones[3][0]["text"] != ""):
            return True

        return False

    def empate(self):
        for i in range(4):
            for j in range(4):
                if self.botones[i][j]["text"] == "":
                    return False
        return True

    def reiniciar_juego(self):
        # Reiniciar todos los botones
        for i in range(4):
            for j in range(4):
                self.botones[i][j]["text"] = ""

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    juego = JuegoCuatroEnRaya(ventana_principal)
    ventana_principal.mainloop()
